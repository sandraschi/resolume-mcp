"""MCP tools for resolume-mcp VJ control."""


def register_all(mcp):
    """Register all tools on the given FastMCP instance."""
    from .help import register_help
    from .resource_manager import register_resource_tools
    from .status import register_status

    register_help(mcp)
    register_status(mcp)
    register_resource_tools(mcp)
