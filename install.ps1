# Installs Claude Code skills to ~/.claude/commands/
$commandsDir = "$env:USERPROFILE\.claude\commands"
New-Item -ItemType Directory -Force -Path $commandsDir | Out-Null
Copy-Item -Verbose "claude\commands\*.md" $commandsDir
Write-Host "Skills installed to $commandsDir"
