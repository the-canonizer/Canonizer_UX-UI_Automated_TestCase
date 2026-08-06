# Simple Test Execution Steps

## 1) Open terminal in project
Run all commands from:

`/Users/ajay/Desktop/Canonizer/Canonizer_UX-UI_Automated_TestCase`

## 2) Activate virtual environment
```bash
source .venv/bin/activate
```

## 3) Set login credentials (optional)
If you ran `./setup.sh`, it may already have saved credentials in `.env.local`.
Otherwise set them in your shell:

```bash
export CANONIZER_DEFAULT_USER="your_email@example.com"
export CANONIZER_DEFAULT_PASS="your_password"
```

Or copy the template and edit it:

```bash
cp .env.local.example .env.local
```

## 4) Run all tests
```bash
./run_tests.sh -v
```

## 5) Run with summary report output
```bash
./run_tests.sh -v --showcase-report-file showcase_test_results.json
```

## 6) Run one test only (example)
```bash
./run_tests.sh -v -k test_login_to_canonizer
```

## 7) Deactivate environment
```bash
deactivate
```
