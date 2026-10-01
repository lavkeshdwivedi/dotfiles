---
description: Keep Windows from sleeping or locking (pass "stop" to turn off)
allowed-tools: PowerShell, Bash
---

Argument: `$ARGUMENTS`

If the argument is `stop` or `off`, stop any running keep-awake process with PowerShell:

```powershell
Get-CimInstance Win32_Process -Filter "CommandLine LIKE '%keep-awake.ps1%'" | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
```

Then reply "Keep awake off." and nothing else.

Otherwise, first check whether it's already running (same CIM query). If it is, reply "Keep awake is already on." Otherwise start it detached with PowerShell:

```powershell
Start-Process powershell.exe -WindowStyle Hidden -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-File',"$env:USERPROFILE\.claude\scripts\keep-awake.ps1"
```

Then reply "Keep awake on. Run /keep-awake stop or right-click the coffee cup tray icon to turn it off." and nothing else.
