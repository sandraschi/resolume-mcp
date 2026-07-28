"""Multilevel help system for resolume-mcp."""

from typing import Annotated

from pydantic import Field


def register_help(mcp):
    @mcp.tool()
    async def help(
        level: Annotated[str, Field(description="Help detail level: basic, intermediate, advanced, expert")] = "basic",
        topic: Annotated[str | None, Field(description="Specific topic: tools, config, examples")] = None,
    ) -> str:
        """Comprehensive help system with multiple knowledge levels.

        This tool provides contextual assistance at different depth levels:

        LEVELS:
        - basic: Quick start and essential commands
        - intermediate: Detailed tool descriptions and workflows
        - advanced: Technical architecture and patterns
        - expert: Development and troubleshooting

        TOPICS:
        - tools: Complete tool reference
        - config: Configuration options
        - examples: Usage examples
        - troubleshooting: Common issues and solutions

        ## Return Format
        {"content": str}

        ## Examples
        help()
        help('intermediate', 'tools')
        help('expert', 'troubleshooting')
        """

        help_content = f"""# resolume-mcp VJ Help - Level: {level}

## Quick Start for VJs

```python
# Load a video clip
clip_control('load', layer=1, clip=1, file_path='C:/videos/my_clip.mp4')

# Trigger playback
clip_control('trigger', layer=1, clip=1)

# Mix layers with opacity
layer_control('opacity', layer=2, value=0.7)

# Set BPM for tempo effects
performance_control('bpm', bpm=128.0)
```

## VJ Workflow Tools

### Clip Management
- **clip_control**: Load, trigger, position, opacity control
- Load videos, control playback, mix clips in real-time

### Layer Control
- **layer_control**: Opacity, blending, transitions
- Mix layers, apply blend modes, smooth transitions

### Effects & Parameters
- **effect_control**: Parameter automation, effect bypassing
- Control visual effects, automate parameters

### Performance Control
- **performance_control**: BPM sync, batch operations
- Tempo-synced effects, atomic parameter changes

## Resolume Setup

### OSC Configuration
1. Open Resolume Arena → Preferences → OSC
2. Enable OSC: ✅
3. Incoming Port: 7000
4. Outgoing Port: 7001
5. Send OSC Feedback: ✅ (optional)

### Layer/Clip Numbers
- Layers: 1-8 (typical setup)
- Clips: 1-10 per layer
- Effects: 1-4 per layer

## Live Performance Tips

### Preparation
- Preload clips before performance
- Test OSC connection with status()
- Set BPM before starting

### During Performance
- Use batch_update for complex transitions
- Layer opacity for smooth mixing
- Effect parameters for real-time manipulation

### Emergency Controls
- layer_control('bypass', layer=X, enabled=False) to disable layers
- clip_control('clear', layer=X, clip=Y) to remove clips
- status('basic', 'resolume') to check connection
"""

        return help_content
