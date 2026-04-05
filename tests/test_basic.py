'''Basic tests for resolume-mcp.'''

import pytest


def test_package_import():
    '''Test that package can be imported.'''
    import resolume_mcp
    assert resolume_mcp.__version__ == '0.1.0'


def test_tools_import():
    '''Test that tools can be imported.'''
    from resolume_mcp import tools
    assert 'help' in tools.__all__
    assert 'status' in tools.__all__
    assert 'clip_control' in tools.__all__
    assert 'layer_control' in tools.__all__
    assert 'effect_control' in tools.__all__
    assert 'performance_control' in tools.__all__
