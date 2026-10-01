# Keeps Windows awake and unlocked while running. Lives in the system tray.
# Right-click the tray icon and pick "Stop keep awake" to restore normal sleep/lock behavior.

Add-Type -AssemblyName System.Windows.Forms, System.Drawing
Add-Type @"
using System;
using System.Runtime.InteropServices;
public static class KeepAwake {
    [DllImport("kernel32.dll")]
    public static extern uint SetThreadExecutionState(uint esFlags);
    [DllImport("user32.dll")]
    public static extern void keybd_event(byte bVk, byte bScan, uint dwFlags, UIntPtr dwExtraInfo);
}
"@

$ES_CONTINUOUS       = [uint32]'0x80000000'
$ES_SYSTEM_REQUIRED  = [uint32]'0x00000001'
$ES_DISPLAY_REQUIRED = [uint32]'0x00000002'
$VK_F15 = 0x7E
$KEYUP  = 0x0002

$started = Get-Date

$tray = New-Object System.Windows.Forms.NotifyIcon
$iconSize = [System.Windows.Forms.SystemInformation]::SmallIconSize
$icons = @{
    Light = New-Object System.Drawing.Icon "$PSScriptRoot\keep-awake-black.ico", $iconSize
    Dark  = New-Object System.Drawing.Icon "$PSScriptRoot\keep-awake-white.ico", $iconSize
}
$themeKey = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize'
$syncIcon = {
    # Taskbar follows the system (not app) theme
    $light = (Get-ItemProperty $themeKey -Name SystemUsesLightTheme -ErrorAction SilentlyContinue).SystemUsesLightTheme -eq 1
    $want = if ($light) { $icons.Light } else { $icons.Dark }
    if ($tray.Icon -ne $want) { $tray.Icon = $want }
}
& $syncIcon
$tray.Text = 'Keep Awake: on'
$tray.Visible = $true

$menu = New-Object System.Windows.Forms.ContextMenuStrip
$stopItem = $menu.Items.Add('Stop keep awake')
$stopItem.add_Click({ [System.Windows.Forms.Application]::Exit() })
$tray.ContextMenuStrip = $menu

$tick = {
    # Block system sleep and display timeout
    [KeepAwake]::SetThreadExecutionState($ES_CONTINUOUS -bor $ES_SYSTEM_REQUIRED -bor $ES_DISPLAY_REQUIRED) | Out-Null
    # Tap F15 (no-op key) to reset the idle timer so the session doesn't auto-lock
    [KeepAwake]::keybd_event($VK_F15, 0, 0, [UIntPtr]::Zero)
    [KeepAwake]::keybd_event($VK_F15, 0, $KEYUP, [UIntPtr]::Zero)
    $tray.Text = 'Keep Awake: on for {0:hh\:mm}' -f ((Get-Date) - $started)
}

$timer = New-Object System.Windows.Forms.Timer
$timer.Interval = 50000
$timer.add_Tick($tick)
$timer.Start()
& $tick

$themeTimer = New-Object System.Windows.Forms.Timer
$themeTimer.Interval = 2000
$themeTimer.add_Tick($syncIcon)
$themeTimer.Start()

try {
    [System.Windows.Forms.Application]::Run()
}
finally {
    $timer.Stop()
    $themeTimer.Stop()
    $tray.Visible = $false
    $tray.Dispose()
    [KeepAwake]::SetThreadExecutionState($ES_CONTINUOUS) | Out-Null
}
