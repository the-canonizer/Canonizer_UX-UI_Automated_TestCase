# Canonizer_UX-UI_Automated_TestCase

Python + Selenium UI automation for Canonizer, driven by pytest.

For the shortest path to a running test, see [SIMPLE_TEST_EXECUTION.md](SIMPLE_TEST_EXECUTION.md).

## Overview

A page-object suite covering authentication, topics, camps, statements, forum
and news, browse and search, profile, uploads and account settings.

| Piece | Where |
| --- | --- |
| Test cases | `test_suites/*_tests.py` |
| Suite composition | `main.py` (`TestPages` mixes the modules together) |
| Page objects | `Canonizer*Page.py`, `CanonizerCampForum.py`, `CanonizerUploadFile.py` |
| Locators | `Identifiers.py` |
| Environment URLs and test data | `Config.py` |
| Shared imports for test modules | `test_suites/shared.py` |
| Login helper, browser attachment | `test_suites/base_flow.py` |
| Browser fixtures, reporting, failure artifacts | `conftest.py`, `pytest.ini` |
| Generated upload images | `test_assets.py` |

The suite targets the deployed environments configured in `Config.py`, primarily
`https://ux-dev.canonizer.com/`.

Current size: **263 collected tests** — 256 executable plus 7 `xfail` backlog
placeholders in `test_suites/backlog_tests.py`.

## Prerequisites

- Python 3.9+
- Google Chrome installed
- Network access to the configured Canonizer environment

## Setup

```sh
./setup.sh
```

On Windows PowerShell:

```powershell
.\setup.ps1
```

The script creates `.venv`, installs `requirements.txt`, and creates `.env.local`
from `.env.local.example` so you can store local credentials.

Manual equivalent:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configure Credentials

Login-required tests read credentials from environment variables:

- `CANONIZER_DEFAULT_USER`
- `CANONIZER_DEFAULT_PASS`

```sh
export CANONIZER_DEFAULT_USER="your_email@example.com"
export CANONIZER_DEFAULT_PASS="your_password"
```

Or put them in `.env.local` (git-ignored); `run_tests.sh` sources it automatically.

If they are missing, any test that calls `login_to_canonizer_app()` now fails
immediately with a clear message rather than silently submitting a blank form.

Note: encrypting these is not useful here, because the Selenium login flow needs
the plaintext password at runtime. Keeping them out of source control is the point.

## Verify Installation

```sh
python -m pytest --collect-only main.py
```

## Run Tests

```sh
./run_tests.sh                                   # everything
./run_tests.sh -k test_click_on_join_now -q      # one smoke test
./run_tests.sh -v                                # verbose
./run_tests.sh -m smoke -q                       # smoke only
./run_tests.sh -m "regression and not destructive" -q
./run_tests.sh -m destructive -q                 # use a safe environment
```

On Windows PowerShell, use `.\run_tests.ps1` with the same arguments.

### Browsers

The browser is built by the `driver` fixture in `conftest.py`, one session per
test. Pick which one with `--browser` (or `CANONIZER_BROWSER`):

```sh
./run_tests.sh --browser chrome -m smoke -q
./run_tests.sh --browser firefox -m smoke -q
./run_tests.sh --browser edge -m smoke -q
```

One browser per run; cover several with a CI matrix. Selenium 4.6+ downloads the
matching driver binary itself, so nothing has to be checked in.

Run headless with the `--headless` flag or `CANONIZER_HEADLESS=1`:

```sh
./run_tests.sh --headless -m smoke -q
CANONIZER_HEADLESS=1 ./run_tests.sh -m smoke -q
```

The implicit wait defaults to 30s and can be tuned with
`CANONIZER_IMPLICIT_WAIT` while the suite migrates to explicit waits.

Showcase summary, printed to the terminal and written as JSON:

```sh
./run_tests.sh --showcase-report-file showcase_test_results.json
```

It reports passed / failed / skipped / xfailed / xpassed counts and flags a
partial success.

### Markers

Markers are applied automatically in `main.py` by `_apply_test_markers()`:

- `regression` — every test
- `smoke` — a named short list of core health checks
- `destructive` — name contains delete/remove/update/edit/create_/upload; these
  create or modify data in the target environment
- `slow` — upload, search, history and notification flows
- `no_browser` — test needs no browser session, so none is started (currently
  the backlog placeholders)

### Failure artifacts

When a test fails, `conftest.py` writes a screenshot, the page DOM and the current
URL to `artifacts/<browser>/<nodeid>.{png,html,url.txt}`. The directory is
git-ignored, and namespaced by browser so a matrix run does not overwrite itself.

### Upload fixtures

`test_assets.py` generates the images the upload tests need — one PNG over the
5 MB limit and one under it — into `.test_assets/` on first use. No local files
need setting up.

## Run Tests In VS Code

Tests are composed into `main.py`, which does not match pytest's default
`test_*.py` discovery pattern, so discovery must point directly at `main.py`.
`.vscode/settings.json`, `launch.json` and `tasks.json` are already wired up.

1. Open the workspace root containing `Canonizer_UX-UI_Automated_TestCase`.
2. `Python: Select Interpreter` → `.venv/bin/python`.
3. `Python: Configure Tests` → pytest.
4. `Testing: Refresh Tests`.

If run icons do not appear: `Testing: Refresh Tests`, then
`Developer: Reload Window`, then reopen `main.py`.

Available tasks: `canonizer: setup`, `canonizer: run all tests`,
`canonizer: run filtered tests`, `canonizer: run smoke tests`,
`canonizer: run non-destructive regression`.

## Test Inventory

[TEST_INVENTORY.md](TEST_INVENTORY.md) groups coverage by feature area.
[REMAINING_TEST_GAPS.md](REMAINING_TEST_GAPS.md) tracks what is not yet covered.

## Project Structure

```text
Canonizer_UX-UI_Automated_TestCase/
├── main.py                        # composes TestPages from the suite mixins, applies markers
├── conftest.py                    # browser fixtures, showcase report, failure screenshots
├── test_assets.py                 # generates upload test images on demand
├── pytest.ini                     # marker registry
├── Config.py                      # URLs, credentials, test data
├── Identifiers.py                 # all locators
├── CanonizerBase.py               # Page base class: safe_click, set_input_value, waits
├── CanonizerTestCases.py          # test-case descriptions printed during runs
├── CanonizerValidationCheckMessages.py
├── test_suites/
│   ├── shared.py                  # common imports for every suite module
│   ├── base_flow.py               # attaches the driver fixture, login helper
│   ├── auth_registration_tests.py
│   ├── topic_tests.py
│   ├── camp_tests.py
│   ├── statement_tests.py
│   ├── forum_news_tests.py
│   ├── browse_search_tests.py
│   ├── profile_upload_access_tests.py
│   ├── misc_tests.py
│   └── backlog_tests.py           # xfail placeholders for unimplemented coverage
├── CanonizerLoginPage.py
├── CanonizerAuthenticationPage.py
├── CanonizerRegistrationPage.py
├── CanonizerCreateUpdateTopicPage.py
├── CanonizerCreateUpdateCampPage.py
├── CanonizerCampStatementPage.py
├── CanonizerCampForum.py
├── CanonizerBrowsePage.py
├── CanonizerSearchPage.py
├── CanonizerAddEditNewsPage.py
├── CanonizerAccountPage.py
├── CanonizerAdvancedSettingsPage.py
├── CanonizerProfileUpdatePage.py
└── CanonizerUploadFile.py
```

## How The Framework Works

- Each `test_suites/*_tests.py` module defines a plain mixin class of test methods.
- `main.py` combines them into a single `TestPages` class, which is what pytest
  discovers, then applies markers to every method.
- The `driver` fixture in `conftest.py` builds a browser, lands it on the base
  URL, and quits it after each test. `BaseFlow` attaches it to the test instance
  via an autouse fixture, so tests keep using `self.driver`.
- Page objects wrap the workflows; `CanonizerBase.Page` supplies `safe_click()`
  and `set_input_value()`, which retry through loading overlays and stale elements.
- `Config.py` centralizes environment URLs, credentials and test data.

## Known Limitations

- **Serial execution.** No `pytest-xdist`; a full run is long. The browser is
  function-scoped so it parallelizes cleanly, but the suite shares environment
  data (topics, camps, one login account), which has to be sorted out first.
- **Firefox and Edge are wired but unproven.** The fixtures exist; the locators
  have only ever been exercised against Chrome, so expect failures to fix.
- **Mixed waits.** `implicitly_wait(30)` is set alongside explicit `WebDriverWait`
  calls. Selenium advises against combining them, and any legitimately empty
  `find_elements()` blocks for the full 30 seconds.
- **Fragile locators.** Of 719 locators, 381 are XPath, ~70 absolute
  (`/html/body/div[1]/...`) and ~183 index-based; only 4 use `data-testid`.
  This is the main source of flakiness.
- **No cleanup.** Destructive tests leave topics, camps and threads behind in the
  target environment permanently.
- **No CI.** There is no pipeline configuration in the repository.
- **Shared environment state.** Some tests assume data created by earlier runs
  and can be order-dependent.

## Recommended First Run

```sh
source .venv/bin/activate
python -m pytest --collect-only main.py
python -m pytest main.py -k test_click_on_join_now -q
```

If the smoke test passes, expand to a subset before attempting the full suite.
