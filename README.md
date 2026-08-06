# Canonizer_UX-UI_Automated_TestCase

Python Selenium UI automation tests for Canonizer.

## Quick Start

For the shortest path to run tests, see [SIMPLE_TEST_EXECUTION.md](SIMPLE_TEST_EXECUTION.md).

## Overview

This repository contains a page-object based UI automation suite.

- Test entry point: `main.py`
- Test runner: `pytest`
- Browser automation: `selenium`
- Page objects: `Canonizer*Page.py`
- Locators: `Identifiers.py`
- Test data and environment config: `Config.py`

The suite currently targets deployed Canonizer environments configured in `Config.py`, including `https://ux-dev.canonizer.com/`.

## Prerequisites

- Python 3.9+
- Google Chrome installed
- Network access to the configured Canonizer environment

## Environment Notes

- Many tests use the URLs and credentials defined in `Config.py`.
- Some tests create or modify data in the target environment.
- Some upload tests use machine-specific file paths and will need local adjustment before they can pass on another machine.

## Setup

From this repository root, run the bootstrap script:

```sh
./setup.sh
```

On Windows PowerShell:

```powershell
.\setup.ps1
```

The script creates `.venv`, installs dependencies from `requirements.txt`, and can store your local login credentials in `.env.local`.

On first run, it also creates `.env.local` from `.env.local.example`.

If you prefer to do it manually, the equivalent commands are:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configure Credentials

The suite reads the main login credentials from `Config.py`. It now also supports environment-variable overrides, which is the safer option because the password does not need to be edited in the repository.

Supported variables:

- `CANONIZER_DEFAULT_USER`
- `CANONIZER_DEFAULT_PASS`

Example:

```sh
export CANONIZER_DEFAULT_USER="your_email@example.com"
export CANONIZER_DEFAULT_PASS="your_password"
```

Alternative:

```sh
cp .env.local.example .env.local
```

Then run the tests in the same terminal session.

Note: this is better than hardcoding the password in source control. True encryption is not especially useful for this test suite, because the Selenium login flow still needs the plaintext password at runtime.

## Verify Installation

Collect the test suite without running browser actions:

```sh
python -m pytest --collect-only main.py
```

At the time this README was updated, the suite collected 191 tests.

## Run Tests

Run a single smoke test:

```sh
./run_tests.sh -k test_click_on_join_now -q
```

On Windows PowerShell:

```powershell
.\run_tests.ps1 -k test_click_on_join_now -q
```

Run a single named test:

```sh
./run_tests.sh -k test_login_to_canonizer -q
```

Run the full suite:

```sh
./run_tests.sh
```

Generate a showcase-friendly summary file while running the suite:

```sh
./run_tests.sh --showcase-report-file showcase_test_results.json
```

This prints a terminal summary with the tests that ran, passed, failed, skipped, and whether the run was a partial success. It also writes a JSON file with the same information.

Run with verbose output:

```sh
./run_tests.sh -v
```

You can also click the Run button in VS Code while `main.py` is active. That now invokes pytest for this file instead of running it as a plain script.

## Run Tests In VS Code

This suite keeps its tests in `main.py`, which does not match pytest's default test file naming pattern. Because of that, VS Code test discovery must point directly at `main.py`.

The workspace is now preconfigured with `.vscode/settings.json`, `.vscode/launch.json`, and `.vscode/tasks.json`, so the interpreter, pytest discovery, and common run commands are already wired up after clone.

`tasks.json` includes OS-specific commands so the same task labels work on macOS, Linux, and Windows.

Use these steps in VS Code:

1. Open the workspace root that contains `Canonizer_UX-UI_Automated_TestCase`.
2. Select the interpreter from `.venv`.
3. Configure Python testing to use `pytest`.
4. Refresh test discovery.

Recommended VS Code flow:

```text
Cmd+Shift+P
Python: Select Interpreter
Choose Canonizer_UX-UI_Automated_TestCase/.venv/bin/python

Cmd+Shift+P
Python: Configure Tests
Choose pytest
```

Workspace test discovery should use this setting:

```json
{
	"python.testing.pytestArgs": [
		"Canonizer_UX-UI_Automated_TestCase/main.py"
	],
	"python.testing.unittestEnabled": false,
	"python.testing.pytestEnabled": true
}
```

If the `Run Test` links or test icons do not appear in the editor:

1. Run `Testing: Refresh Tests` from the Command Palette.
2. Run `Developer: Reload Window`.
3. Reopen `main.py`.

After discovery succeeds, VS Code should show test run controls above the `TestPages` class and each `test_...` method in `main.py`.

The workspace also includes `.vscode/launch.json` and `.vscode/tasks.json` so you can:

1. Run `Canonizer: Run main.py` from Run and Debug to execute the suite entrypoint.
2. Run `canonizer: setup` to bootstrap the environment from VS Code.
3. Run `canonizer: run all tests` or `canonizer: run filtered tests` from the Tasks menu.

## Test Inventory

If you want one place to review the suite coverage, use [TEST_INVENTORY.md](TEST_INVENTORY.md). It groups the current `main.py` tests by feature area and is the best starting point for implementing the next automation slice.

## Project Structure

```text
Canonizer_UX-UI_Automated_TestCase/
├── main.py
├── Config.py
├── Identifiers.py
├── CanonizerBase.py
├── CanonizerLoginPage.py
├── CanonizerRegistrationPage.py
├── CanonizerCreateUpdateTopicPage.py
├── CanonizerCreateUpdateCampPage.py
├── CanonizerCampStatementPage.py
├── CanonizerCampForum.py
├── CanonizerBrowsePage.py
├── CanonizerAddEditNewsPage.py
├── CanonizerAccountPage.py
├── CanonizerProfileUpdatePage.py
├── CanonizerUploadFile.py
└── CanonizerTestCases.py
```

## How The Framework Works

- `main.py` contains the pytest-discovered test class and test methods.
- `setup_method()` opens Chrome and loads the base URL before each test.
- Page object classes encapsulate workflows for login, registration, topic creation, camp creation, statements, forums, profile settings, and uploads.
- `Config.py` centralizes environment URLs, user credentials, and test input data.

## Known Limitations

- The suite currently uses direct `webdriver.Chrome()` calls in multiple files.
- Chrome and ChromeDriver compatibility must be available on the machine.
- Some tests depend on shared environment state and may be flaky if run repeatedly against the same environment.
- File upload scenarios may fail until local file paths are updated.

## Recommended First Run

Use this order on a new machine:

```sh
source .venv/bin/activate
python -m pytest --collect-only main.py
python -m pytest main.py -k test_click_on_join_now -q
```

If the smoke test passes, expand to a small subset before attempting the entire suite.
