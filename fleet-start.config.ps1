# Per-repo fleet start config for resolume-mcp
# Edit ports/backend target here - start.ps1 is fleet-standard.
@{
    Name         = 'resolume-mcp'
    BackendPort  = 10771
    FrontendPort = 10770
    HealthPath   = '/health'
    WebRoot      = 'D:\Dev\repos\resolume-mcp\web_sota'
    Backend = @{
        Kind          = 'uvicorn'
        UvicornTarget = 'server:app'
        WorkDir       = 'D:\Dev\repos\resolume-mcp\web_sota\backend'
        UvProject     = 'D:\Dev\repos\resolume-mcp'
        SyncExtras    = @('dev')
        Env           = @{ WEB_PORT = '10771' }
    }
    Frontend = @{
        Kind           = 'vite-npm'
        PackageManager = 'npm'
        PortEnvVar     = 'VITE_PORT'
        ApiTargetEnv   = 'VITE_API_TARGET'
    }
}
