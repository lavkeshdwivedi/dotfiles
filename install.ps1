# Installs Claude Code skills to ~/.claude/commands/ and helper scripts to ~/.claude/scripts/
$commandsDir = "$env:USERPROFILE\.claude\commands"
$scriptsDir = "$env:USERPROFILE\.claude\scripts"
New-Item -ItemType Directory -Force -Path $commandsDir, $scriptsDir | Out-Null
Copy-Item -Verbose "claude\commands\*.md" $commandsDir
Copy-Item -Verbose "windows\*.ps1", "windows\*.ico" $scriptsDir
Write-Host "Skills installed to $commandsDir, scripts to $scriptsDir"
