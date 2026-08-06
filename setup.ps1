$ErrorActionPreference = "Stop"

$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$VenvDir = Join-Path $RootDir ".venv"
$EnvFile = Join-Path $RootDir ".env.local"
$EnvTemplate = Join-Path $RootDir ".env.local.example"
$PythonBin = if ($env:PYTHON_BIN) { $env:PYTHON_BIN } else { "python" }

function Get-VenvPython {
    $windowsPython = Join-Path $VenvDir "Scripts/python.exe"
    $posixPython = Join-Path $VenvDir "bin/python"
    if (Test-Path $windowsPython) { return $windowsPython }
    if (Test-Path $posixPython) { return $posixPython }
    return $windowsPython
}

if (-not (Get-Command $PythonBin -ErrorAction SilentlyContinue)) {
    throw "Python was not found in PATH. Install Python 3.9+ and retry."
}

$chromeExe = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chromeExe)) {
    Write-Host "Warning: Google Chrome was not found at '$chromeExe'. Install Chrome before running UI tests."
}

if (-not (Test-Path $VenvDir)) {
    & $PythonBin -m venv $VenvDir
}

$venvPython = Get-VenvPython
& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r (Join-Path $RootDir "requirements.txt")

if (-not (Test-Path $EnvFile)) {
    if (Test-Path $EnvTemplate) {
        Copy-Item $EnvTemplate $EnvFile
        Write-Host "Created .env.local from .env.local.example"
    }

    $canonizerUser = $env:CANONIZER_DEFAULT_USER
    $canonizerPass = $env:CANONIZER_DEFAULT_PASS

    if ([string]::IsNullOrWhiteSpace($canonizerUser)) {
        $canonizerUser = Read-Host "CANONIZER_DEFAULT_USER (leave blank to skip)"
    }

    if ([string]::IsNullOrWhiteSpace($canonizerPass)) {
        $secure = Read-Host "CANONIZER_DEFAULT_PASS (leave blank to skip)" -AsSecureString
        $ptr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
        try {
            $canonizerPass = [System.Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr)
        }
        finally {
            [System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($canonizerUser) -or -not [string]::IsNullOrWhiteSpace($canonizerPass)) {
        $lines = @()
        if (-not [string]::IsNullOrWhiteSpace($canonizerUser)) {
            $lines += "CANONIZER_DEFAULT_USER=$canonizerUser"
        }
        if (-not [string]::IsNullOrWhiteSpace($canonizerPass)) {
            $lines += "CANONIZER_DEFAULT_PASS=$canonizerPass"
        }
        Set-Content -Path $EnvFile -Value $lines -Encoding UTF8
        Write-Host "Saved local credentials to .env.local"
    }
    else {
        Write-Host "Edit .env.local to set CANONIZER_DEFAULT_USER and CANONIZER_DEFAULT_PASS before running login-required tests."
    }
}

Write-Host "Setup complete."
Write-Host "Next steps:"
Write-Host "1. Run all tests: ./run_tests.ps1"
Write-Host "2. Run a single test: ./run_tests.ps1 -k test_login_to_canonizer -q"
Write-Host "3. Run main.py directly from the VS Code Run button; it executes pytest."