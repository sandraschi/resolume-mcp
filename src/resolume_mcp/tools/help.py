'''Multilevel help system for resolume-mcp.

Provides contextual help at multiple knowledge levels.
'''

from fastmcp import FastMCP

mcp = FastMCP('resolume-mcp')


@mcp.tool
async def help(level: str = 'basic', topic: str | None = None) -> str:
    '''Comprehensive help system with multiple knowledge levels.
    
    This tool provides contextual assistance at different depth levels:
    
    LEVELS:
    - basic: Quick start and essential commands
    - intermediate: Detailed tool descriptions and workflows
    - advanced: Technical architecture and patterns
    - expert: Development and troubleshooting
    
    TOPICS:
    - tools: Complete tool reference
    - config: Configuration options
    - examples: Usage examples
    - troubleshooting: Common issues and solutions
    
    Args:
        level (str, default='basic'): Help detail level
        topic (str, optional): Specific topic to focus on
    
    Returns:
        Contextual help content with examples
    
    Examples:
        Basic overview: help()
        Detailed tools: help('intermediate', 'tools')
        Troubleshooting: help('expert', 'troubleshooting')
    '''
    
    help_content = f'''# resolume-mcp Help - Level: {level}
    
## Quick Start

\\\python
# Example usage
from resolume_mcp import resource_manager

# Use the tools...
\\\

## Available Tools

1. **help** - This multilevel help system
2. **status** - System status and diagnostics
3. **resource_manager** - Main operations (customize for your domain)

## Configuration

See docs/user-guide/ for detailed setup instructions.

## Support

- Documentation: See docs/
- Issues: GitHub Issues
- Standards: D:\\Dev\\repos\\mcp-central-docs\\
'''
    
    return help_content
