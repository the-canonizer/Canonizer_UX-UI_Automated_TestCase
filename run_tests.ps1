$ErrorActionPreference = "Stop"

$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$VenvDir = Join-Path $RootDir ".venv"
$WindowsPython = Join-Path $VenvDir "Scripts/python.exe"
$PosixPython = Join-Path $VenvDir "bin/python"
$EnvFile = Join-Path $RootDir ".env.local"

if (Test-Path $WindowsPython) {
    $VenvPython = $WindowsPython
}
elseif (Test-Path $PosixPython) {
    $VenvPython = $PosixPython
}
else {
    throw "Virtual environment not found. Run ./setup.ps1 (Windows) or ./setup.sh (macOS/Linux) first."
}

if (Test-Path $EnvFile) {
    Get-Content $EnvFile | ForEach-Object {
        $line = $_.Trim()
        if (-not $line -or $line.StartsWith("#")) {
            return
        }
        if ($line.StartsWith("export ")) {
            $line = $line.Substring(7)
        }
        $parts = $line -split "=", 2
        if ($parts.Length -eq 2) {
            [Environment]::SetEnvironmentVariable($parts[0], $parts[1], "Process")
        }
    }
}

& $VenvPython (Join-Path $RootDir "main.py") @args
exit $LASTEXITCODE