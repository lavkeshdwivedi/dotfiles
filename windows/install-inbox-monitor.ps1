# Registers the inbox monitor as a Windows scheduled task for the current user.
# Run after storing the app passwords (see claude/commands/inbox-monitor.md).
#   .\install-inbox-monitor.ps1            every 15 minutes
#   .\install-inbox-monitor.ps1 -Minutes 10
#   .\install-inbox-monitor.ps1 -Remove    delete the task
param([int]$Minutes = 15, [switch]$Remove)

$name = 'InboxMonitor'
if ($Remove) {
    schtasks /Delete /TN $name /F
    exit $LASTEXITCODE
}

$py = (Get-Command pythonw -ErrorAction SilentlyContinue).Source
if (-not $py) { $py = (Get-Command python -ErrorAction Stop).Source }
$script = Join-Path $PSScriptRoot 'inbox_monitor.py'
if (-not (Test-Path $script)) { throw "Missing $script" }

# Runs only while you are logged in, so Credential Manager is available. No password is stored here.
schtasks /Create /F /SC MINUTE /MO $Minutes /TN $name /TR "`"$py`" `"$script`""
if ($LASTEXITCODE -eq 0) { Write-Host "Registered $name every $Minutes minutes. Log: $env:LOCALAPPDATA\inbox-monitor\log" }
