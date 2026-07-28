"""Tests for resolume-mcp tools and registration."""


def test_package_import():
    """Test that package can be imported."""
    import resolume_mcp

    assert resolume_mcp.__version__ == "0.1.0"


def test_register_all_function():
    """Test that register_all is callable and accepts an mcp instance."""
    from resolume_mcp import tools

    assert hasattr(tools, "register_all")
    assert callable(tools.register_all)


def test_register_all_succeeds():
    """Test that register_all runs without error on an mcp instance."""
    from fastmcp import FastMCP

    from resolume_mcp.tools import register_all

    mcp = FastMCP("test")
    register_all(mcp)
    assert True
