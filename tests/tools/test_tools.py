'''Tests for MCP tools.'''

import pytest


def test_tools_module():
    '''Test that tools module exports correctly.'''
    from resolume_mcp import tools
    
    assert hasattr(tools, 'help')
    assert hasattr(tools, 'status')
    assert hasattr(tools, 'resource_manager')
    assert len(tools.__all__) == 3


def test_tool_imports():
    '''Test that individual tools can be imported.'''
    from resolume_mcp.tools import help, status, resource_manager
    
    # Tools are FastMCP FunctionTool objects
    assert help is not None
    assert status is not None
    assert resource_manager is not None
