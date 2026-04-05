'''MCP tools for resolume-mcp VJ control.

This package provides comprehensive control over Resolume Arena for live video performances.

Tool Organization:
- help: Multilevel help system for VJ operations
- status: System status, diagnostics, and Resolume connection
- clip_control: Video clip loading, playback, and manipulation
- layer_control: Layer opacity, blending, and transitions
- effect_control: Effect parameter control and bypassing
- performance_control: Global performance parameters and batch operations

All tools use comprehensive docstrings (FastMCP 2.12+ standard).
No description= parameters in @mcp.tool() decorators.
'''

from .help import help
from .status import status
from .resource_manager import clip_control, layer_control, effect_control, performance_control

__all__ = [
    'help',
    'status',
    'clip_control',
    'layer_control',
    'effect_control',
    'performance_control',
]
