"""Tests for MCP tool registration and imports."""


def test_help_module_has_register():
    """Test that help module provides register_help."""
    from resolume_mcp.tools.help import register_help

    assert callable(register_help)


def test_status_module_has_register():
    """Test that status module provides register_status."""
    from resolume_mcp.tools.status import register_status

    assert callable(register_status)


def test_resource_manager_has_register():
    """Test that resource_manager provides register_resource_tools."""
    from resolume_mcp.tools.resource_manager import register_resource_tools

    assert callable(register_resource_tools)
