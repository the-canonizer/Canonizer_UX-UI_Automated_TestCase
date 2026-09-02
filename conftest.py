import json
import os
import re
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from Config import DEFAULT_BASE_URL, DEFAULT_BINARY_LOCATION


REPORT_FILE = Path("showcase_test_results.json")
ARTIFACT_DIR = Path("artifacts")

# Kept configurable so the implicit/explicit wait mix can be tuned (and
# eventually driven to 0) without editing every module.
IMPLICIT_WAIT = int(os.getenv("CANONIZER_IMPLICIT_WAIT", "30"))


# --------------------------------------------------------------------------
# Browser construction
# --------------------------------------------------------------------------
# Selenium 4.6+ resolves the matching driver binary itself (Selenium Manager),
# so no chromedriver/geckodriver needs to be checked into the repository.

def _chrome_driver(headless):
    options = webdriver.ChromeOptions()
    if DEFAULT_BINARY_LOCATION and os.path.exists(DEFAULT_BINARY_LOCATION):
        options.binary_location = DEFAULT_BINARY_LOCATION
    options.add_argument("--start-maximized")
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)


def _firefox_driver(headless):
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)
    return driver


def _edge_driver(headless):
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    return webdriver.Edge(options=options)


BROWSER_FACTORIES = {
    "chrome": _chrome_driver,
    "firefox": _firefox_driver,
    "edge": _edge_driver,
}


def _artifact_name(nodeid):
    """Turn a pytest nodeid into a safe filename stem."""
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", nodeid).strip("_")[:150]


def _capture_failure_artifacts(item, report):
    """Save a screenshot, the DOM and the URL for a failing UI test.

    A red Selenium test says almost nothing on its own; these three files turn
    most failures into a two-minute diagnosis.
    """
    driver = getattr(getattr(item, "instance", None), "driver", None)
    if driver is None:
        return

    try:
        # Namespaced by browser so a matrix run does not overwrite itself.
        out_dir = ARTIFACT_DIR / item.config.getoption("--browser").lower()
        out_dir.mkdir(parents=True, exist_ok=True)
        base = out_dir / _artifact_name(report.nodeid)
        driver.save_screenshot(str(base) + ".png")
        Path(str(base) + ".html").write_text(driver.page_source, encoding="utf-8")
        Path(str(base) + ".url.txt").write_text(driver.current_url, encoding="utf-8")
    except Exception:
        # A dead browser session must not turn into a second, confusing failure.
        pass


def pytest_configure(config):
    config._showcase_results = []

    name = config.getoption("--browser").strip().lower()
    if name not in BROWSER_FACTORIES:
        raise pytest.UsageError(
            "Unknown --browser %r. Choose one of: %s"
            % (name, ", ".join(sorted(BROWSER_FACTORIES)))
        )


def pytest_addoption(parser):
    parser.addoption(
        "--showcase-report-file",
        action="store",
        default=str(REPORT_FILE),
        help="Write a JSON showcase summary to this path.",
    )
    parser.addoption(
        "--browser",
        action="store",
        default=os.getenv("CANONIZER_BROWSER", "chrome"),
        help="Browser to run against: chrome, firefox or edge. One per run; "
             "use a CI matrix to cover several.",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=bool(os.getenv("CANONIZER_HEADLESS")),
        help="Run the browser headless. Also enabled by CANONIZER_HEADLESS=1.",
    )


# --------------------------------------------------------------------------
# Fixtures
# --------------------------------------------------------------------------

@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    """Which browser this run targets. Validated in pytest_configure."""
    return pytestconfig.getoption("--browser").strip().lower()


@pytest.fixture(scope="session")
def headless(pytestconfig):
    """Whether to run without a visible browser window."""
    return bool(pytestconfig.getoption("--headless"))


@pytest.fixture
def driver(browser_name, headless):
    """A browser session for one test, landed on the base URL.

    Function-scoped, so every test gets a clean session and nothing leaks
    between tests. Being a fixture (rather than setup_method) is what lets the
    browser be parametrized and lets tests request tmp_path and friends.
    """
    web_driver = BROWSER_FACTORIES[browser_name](headless)
    try:
        web_driver.implicitly_wait(IMPLICIT_WAIT)
        web_driver.get(DEFAULT_BASE_URL)
        yield web_driver
    finally:
        try:
            web_driver.quit()
        except WebDriverException:
            pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    # pytest reports an xfail as outcome "skipped" (and an xpass as "passed"),
    # flagging both with wasxfail. Without this the xfailed/xpassed counters
    # below were always zero and the backlog tests looked like plain skips.
    outcome_name = report.outcome
    if hasattr(report, "wasxfail"):
        outcome_name = "xpassed" if report.passed else "xfailed"
    elif report.failed:
        _capture_failure_artifacts(item, report)

    results = getattr(item.config, "_showcase_results", None)
    if results is None:
        results = []
        item.config._showcase_results = results

    results.append(
        {
            "nodeid": report.nodeid,
            "outcome": outcome_name,
            "duration": round(report.duration, 3),
        }
    )


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    results = getattr(config, "_showcase_results", [])
    if not results:
        # Nothing ran (for example --collect-only), so leave the previous
        # report in place rather than overwriting it with an empty one.
        return

    passed = [item for item in results if item["outcome"] == "passed"]
    failed = [item for item in results if item["outcome"] == "failed"]
    skipped = [item for item in results if item["outcome"] == "skipped"]
    xfailed = [item for item in results if item["outcome"] == "xfailed"]
    xpassed = [item for item in results if item["outcome"] == "xpassed"]

    report_path = Path(config.getoption("--showcase-report-file")).resolve()
    report_payload = {
        "total": len(results),
        "passed": len(passed),
        "failed": len(failed),
        "skipped": len(skipped),
        "xfailed": len(xfailed),
        "xpassed": len(xpassed),
        "partial_success": bool(passed and failed),
        "tests": results,
    }
    report_path.write_text(json.dumps(report_payload, indent=2), encoding="utf-8")

    terminalreporter.write_sep("=", "Canonizer showcase summary")
    terminalreporter.write_line(f"Total tests run: {len(results)}")
    terminalreporter.write_line(f"Passed: {len(passed)}")
    terminalreporter.write_line(f"Failed: {len(failed)}")
    terminalreporter.write_line(f"Skipped: {len(skipped)}")
    terminalreporter.write_line(f"XFailed: {len(xfailed)}")
    terminalreporter.write_line(f"XPassed: {len(xpassed)}")
    terminalreporter.write_line(
        f"Partial success: {'yes' if passed and failed else 'no'}"
    )
    terminalreporter.write_line(f"Report file: {report_path}")

    if passed:
        terminalreporter.write_line("\nPassed tests:")
        for item in passed:
            terminalreporter.write_line(f"  PASS {item['nodeid']} ({item['duration']}s)")

    if failed:
        terminalreporter.write_line("\nFailed tests:")
        for item in failed:
            terminalreporter.write_line(f"  FAIL {item['nodeid']} ({item['duration']}s)")

    if xfailed:
        terminalreporter.write_line("\nExpected failures:")
        for item in xfailed:
            terminalreporter.write_line(f"  XFAIL {item['nodeid']} ({item['duration']}s)")

    if xpassed:
        terminalreporter.write_line("\nUnexpected passes:")
        for item in xpassed:
            terminalreporter.write_line(f"  XPASS {item['nodeid']} ({item['duration']}s)")
