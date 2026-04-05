'''Tests for MCP tools.'''

import pytest


def test_tools_module():
    '''Test that tools module exports correctly.'''
    from resolume_mcp import tools

    assert hasattr(tools, 'help')
    assert hasattr(tools, 'status')
    assert hasattr(tools, 'clip_control')
    assert hasattr(tools, 'layer_control')
    assert hasattr(tools, 'effect_control')
    assert hasattr(tools, 'performance_control')
    assert len(tools.__all__) == 6


def test_tool_imports():
    '''Test that individual tools can be imported.'''
    from resolume_mcp.tools import help, status, clip_control, layer_control, effect_control, performance_control

    # Tools are FastMCP FunctionTool objects
    assert help is not None
    assert status is not None
    assert clip_control is not None
    assert layer_control is not None
    assert effect_control is not None
    assert performance_control is not None
