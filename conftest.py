import json
from pathlib import Path

import pytest


REPORT_FILE = Path("showcase_test_results.json")


def pytest_configure(config):
    config._showcase_results = []


def pytest_addoption(parser):
    parser.addoption(
        "--showcase-report-file",
        action="store",
        default=str(REPORT_FILE),
        help="Write a JSON showcase summary to this path.",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    results = getattr(item.config, "_showcase_results", None)
    if results is None:
        results = []
        item.config._showcase_results = results

    results.append(
        {
            "nodeid": report.nodeid,
            "outcome": report.outcome,
            "duration": round(report.duration, 3),
        }
    )


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    results = getattr(config, "_showcase_results", [])
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
