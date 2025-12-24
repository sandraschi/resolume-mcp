'''MCP tools for resolume-mcp.

This package provides portmanteau tools following the hub-and-spoke pattern
documented in mcp-central-docs/patterns/PORTMANTEAU_CONCEPT.md

Tool Organization:
- help: Multilevel help system
- status: System status and diagnostics
- resource_manager: Main portmanteau tool (customize for your domain)

All tools use comprehensive docstrings (FastMCP 2.12+ standard).
No description= parameters in @mcp.tool() decorators.
'''

from .help import help
from .resource_manager import resource_manager
from .status import status

__all__ = [
    'help',
    'resource_manager',
    'status',
]
