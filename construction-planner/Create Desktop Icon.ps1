# Creates a desktop shortcut that opens the Planner Suite home page
# (ConstructSim 3D, FlowForge flowchart maker, and IdeaBoard whiteboard).
# Right-click this file -> "Run with PowerShell", or run it from a PowerShell window.

$proj    = Split-Path -Parent $MyInvocation.MyCommand.Path
$target  = Join-Path $proj "home.html"
$icon    = Join-Path $proj "assets\suite.ico"
$desktop = [Environment]::GetFolderPath("Desktop")
$lnkPath = Join-Path $desktop "Construction Planner Suite.lnk"

$ws = New-Object -ComObject WScript.Shell
$sc = $ws.CreateShortcut($lnkPath)
$sc.TargetPath        = $target
$sc.WorkingDirectory  = $proj
$sc.IconLocation      = "$icon,0"
$sc.Description        = "Open the Planner Suite home (3D Planner, FlowForge, IdeaBoard)"
$sc.Save()

# Clean up the old flowchart-only shortcut if it exists
$old = Join-Path $desktop "FlowForge Flowchart Maker.lnk"
if (Test-Path $old) { Remove-Item $old -Force }

if (Test-Path $lnkPath) {
  Write-Host "Desktop icon created: $lnkPath" -ForegroundColor Green
} else {
  Write-Host "Failed to create the desktop icon." -ForegroundColor Red
}
