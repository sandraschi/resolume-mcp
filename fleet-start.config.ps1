# Per-repo fleet start config for resolume-mcp
# Edit ports/backend target here - start.ps1 is fleet-standard.
@{
    Name         = 'resolume-mcp'
    BackendPort  = 11140
    FrontendPort = 11139
    HealthPath   = '/health'
    WebRoot      = 'web_sota'
    Backend = @{
        Kind          = 'uvicorn'
        UvicornTarget = 'web_sota.backend.server:app'
        SyncExtras    = @('dev')
        Env           = @{ WEB_PORT = '11140' }
    }
    Frontend = @{
        Kind           = 'vite-npm'
        PackageManager = 'npm'
        PortEnvVar     = 'VITE_PORT'
        ApiTargetEnv   = 'VITE_API_TARGET'
    }
}
