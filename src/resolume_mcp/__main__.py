"""Main entry point for resolume-mcp MCP server."""

from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

from resolume_mcp import tools

from .transport import run_server

mcp = FastMCP("resolume-mcp")

# Register tools — the tool modules accept the mcp instance and register on it
tools.register_all(mcp)


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    return JSONResponse({"status": "healthy", "server": "resolume-mcp"})


def main():
    """Run the MCP server."""
    run_server(mcp, server_name="resolume-mcp")


if __name__ == "__main__":
    main()
