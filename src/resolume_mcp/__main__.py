'''Main entry point for resolume-mcp MCP server.'''

from fastmcp import FastMCP
from resolume_mcp import tools
from .transport import run_server
from starlette.requests import Request
from starlette.responses import JSONResponse

mcp = FastMCP('resolume-mcp')


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    return JSONResponse({"status": "healthy", "server": "resolume-mcp"})


def main():
    '''Run the MCP server.'''
    run_server(mcp, server_name="resolume-mcp")


if __name__ == '__main__':
    main()