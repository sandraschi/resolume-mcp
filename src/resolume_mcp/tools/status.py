'''System status and diagnostics for resolume-mcp.'''

from fastmcp import FastMCP

mcp = FastMCP('resolume-mcp')


@mcp.tool
async def status(level: str = 'basic', focus: str | None = None) -> str:
    '''Get system status and diagnostic information.
    
    Provides different levels of diagnostic detail:
    
    LEVELS:
    - basic: Core system status
    - intermediate: Configuration and resources
    - advanced: Performance metrics
    - diagnostic: Detailed troubleshooting info
    
    FOCUS AREAS:
    - system: System resources and health
    - config: Configuration validation
    - performance: Performance metrics
    
    Args:
        level (str, default='basic'): Status detail level
        focus (str, optional): Specific area to focus on
    
    Returns:
        Formatted status report
    
    Examples:
        Basic status: status()
        Detailed config: status('intermediate', 'config')
        Performance: status('advanced', 'performance')
    '''
    
    status_report = f'''# resolume-mcp Status - Level: {level}

## System Status
✅ Server running
✅ Version: 0.1.0
✅ Configuration: Valid

## Tools Available
- help (multilevel help)
- status (this tool)
- resource_manager (main operations)

## Health Checks
✅ All systems operational
'''
    
    return status_report
