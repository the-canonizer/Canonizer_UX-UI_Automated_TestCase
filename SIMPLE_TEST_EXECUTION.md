# Simple Test Execution Steps

## 1) Open terminal in project
Run all commands from:

`/Users/ajay/Desktop/Canonizer/Canonizer_UX-UI_Automated_TestCase`

## 2) Activate virtual environment
```bash
source .venv/bin/activate
```

## 3) Set login credentials (required)
```bash
export CANONIZER_DEFAULT_USER="your_email@example.com"
export CANONIZER_DEFAULT_PASS="your_password"
```

## 4) Run all tests
```bash
pytest -v main.py
```

## 5) Run with summary report output
```bash
pytest -v main.py --showcase-report-file ../showcase_test_results.json
```

## 6) Run one test only (example)
```bash
pytest -v main.py::TestPages::test_login_to_canonizer
```

## 7) Deactivate environment
```bash
deactivate
```
