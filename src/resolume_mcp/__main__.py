'''Main entry point for resolume-mcp MCP server.'''

from fastmcp import FastMCP
from resolume_mcp import tools
from .transport import run_server

mcp = FastMCP('resolume-mcp')


def main():
    '''Run the MCP server.'''
    run_server(mcp, server_name="resolume-mcp")


if __name__ == '__main__':
    main()