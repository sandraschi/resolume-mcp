Param(
    [switch]$Headless,
    [switch]$BackendOnly,
    [switch]$FrontendOnly,
    [switch]$NoBrowser,
    [switch]$ReuseIfRunning
)

# --- SOTA Headless Standard ---
if ($Headless -and ($Host.UI.RawUI.WindowTitle -notmatch 'Hidden')) {
    Start-Process pwsh -ArgumentList '-NoProfile', '-File', $PSCommandPath, '-Headless' -WindowStyle Hidden
    exit
}
$WindowStyle = if ($Headless) { 'Hidden' } else { 'Normal' }
# ------------------------------

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$FleetStartPath = Join-Path $ProjectRoot "scripts\FleetStartMode.ps1"
if (-not (Test-Path -LiteralPath $FleetStartPath)) {
    Write-Host "ERROR: Missing vendored launcher helper: $FleetStartPath" -ForegroundColor Red
    exit 1
}
. $FleetStartPath
$FleetStart = Initialize-FleetStartMode @PSBoundParameters
Enter-FleetHeadlessConsole -Headless:$Headless -BackendOnly:$BackendOnly

# Webapp Start - Standardized SOTA
$WebPort = 10770
$BackendPort = 10771

$portResolve = @{
    Ports      = @($WebPort, $BackendPort)
    Label      = "resolume-mcp"
    AllowReuse = $ReuseIfRunning
}
if ($ReuseIfRunning) {
    $portResolve.HealthChecks = @{
        $WebPort     = "http://127.0.0.1:$WebPort/"
        $BackendPort = $null  # FastMCP server — no HTTP health endpoint
    }
}
$portState = Resolve-FleetPortConflict @portResolve
if ($portState.Action -eq 'Blocked') { exit 1 }
if ($portState.Reuse) { return }

# 2. Setup
Set-Location $PSScriptRoot
if (-not (Test-Path "node_modules")) { npm install }
uv sync

# 3. Start the Python backend (Background)
Write-Host "Starting Python backend on port $BackendPort ..." -ForegroundColor Cyan
$backendCmd = "`$env:PYTHONPATH = '$PSScriptRoot;$PSScriptRoot\src'; Set-Location '$PSScriptRoot'; uv run python -m resolume_mcp --http --port $BackendPort"
Start-Process powershell -ArgumentList "-NoExit", "-Command", $backendCmd -WindowStyle Normal

# 3b. Wait for backend to be ready
Write-Host "Waiting for backend on port $BackendPort ..." -ForegroundColor Cyan
for ($i = 0; $i -lt 30; $i++) {
    try { $null = Invoke-WebRequest -Uri "http://127.0.0.1:$BackendPort/health" -TimeoutSec 2 -UseBasicParsing -ErrorAction Stop; Write-Host "Backend ready!" -ForegroundColor Green; break }
    catch { Start-Sleep -Seconds 1 }
}

# 4. Run server (Vite dev)
if (-not $FleetStart.RunFrontend) { return }
Write-Host "Starting Vite frontend on port $WebPort ..." -ForegroundColor Green
$frontendUrl = "http://127.0.0.1:$WebPort/"
$pollAndOpen = "for (`$i = 0; `$i -lt 60; `$i++) { try { `$null = Invoke-WebRequest -Uri '$frontendUrl' -TimeoutSec 2 -UseBasicParsing -ErrorAction Stop; Start-Process '$frontendUrl'; exit } catch { Start-Sleep -Seconds 1 } }"
Start-Process powershell -ArgumentList "-NoProfile", "-WindowStyle", "Hidden", "-Command", $pollAndOpen
Write-Host "Browser will open automatically when Vite is ready." -ForegroundColor Gray
npm run dev -- --port $WebPort --host




