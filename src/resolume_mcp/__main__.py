'''Main entry point for resolume-mcp MCP server.'''

from fastmcp import FastMCP
from resolume_mcp import tools

mcp = FastMCP('resolume-mcp')


def main():
    '''Run the MCP server.'''
    mcp.run()


if __name__ == '__main__':
    main()
