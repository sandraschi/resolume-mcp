# VJ Workflow Guide - resolume-mcp

**Live Video Performance Control with Natural Language**

**Last Updated:** 2025-12-24

---

## 🎬 Overview

This guide shows how to use resolume-mcp for live VJ performances. Control Resolume Arena through natural language commands in Claude Desktop for seamless video mixing and effects.

---

## 🚀 Quick Setup

### 1. Resolume Configuration

**Required Settings in Resolume Arena:**

```
Preferences → OSC
├── Enable OSC: ✅
├── Incoming Port: 7000
├── Outgoing Port: 7001
└── Send OSC Feedback: ✅ (recommended)
```

### 2. Claude Desktop Setup

Add to `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "resolume-mcp": {
      "command": "python",
      "args": ["-m", "resolume_mcp"]
    }
  }
}
```

### 3. Test Connection

Ask Claude: *"Check Resolume connection status"*

Expected response includes: `✅ Connected to Resolume Arena`

---

## 🎛️ Core VJ Tools

### Clip Control (`clip_control`)

**Load and manipulate video clips in real-time.**

| Operation | Description | Example |
|-----------|-------------|---------|
| `load` | Load video file into clip slot | `clip_control('load', layer=1, clip=1, file_path='C:/videos/clip.mp4')` |
| `trigger` | Start playback from beginning | `clip_control('trigger', layer=1, clip=1)` |
| `position` | Set playback position (0.0-1.0) | `clip_control('position', layer=1, clip=1, position=0.5)` |
| `opacity` | Set clip opacity (0.0-1.0) | `clip_control('opacity', layer=1, clip=1, opacity=0.8)` |
| `clear` | Remove clip from slot | `clip_control('clear', layer=1, clip=1)` |

**Natural Language Examples:**
- *"Load my video clip into layer 1"*
- *"Start playing clip 2 on layer 1"*
- *"Set clip position to halfway through"*
- *"Make clip 1 70% transparent"*

### Layer Control (`layer_control`)

**Control layer properties and mixing.**

| Operation | Description | Values |
|-----------|-------------|--------|
| `opacity` | Layer transparency | 0.0 (invisible) - 1.0 (opaque) |
| `bypass` | Enable/disable layer | `true`/`false` |
| `blend_mode` | Blending algorithm | 0-11 (see blend modes below) |
| `transition` | Transition duration | seconds (e.g., 2.0) |

**Blend Modes:**
```
0: Normal     1: Add        2: Subtract   3: Multiply
4: Screen     5: Overlay    6: Hard Light 7: Soft Light
8: Dodge      9: Burn      10: Darken    11: Lighten
```

**Natural Language Examples:**
- *"Set layer 2 to 50% opacity"*
- *"Switch layer 1 to Add blend mode"*
- *"Disable layer 3"*
- *"Make layer transitions 3 seconds long"*

### Effect Control (`effect_control`)

**Automate visual effects parameters.**

| Operation | Description | Parameters |
|-----------|-------------|------------|
| `parameter` | Set effect parameter value | `layer`, `effect`, `parameter`, `value` |
| `bypass` | Enable/disable effect | `layer`, `effect`, `enabled` |

**Natural Language Examples:**
- *"Set effect 1 parameter 1 to 0.8 on layer 1"*
- *"Disable the blur effect on layer 2"*

### Performance Control (`performance_control`)

**Global performance and batch operations.**

| Operation | Description | Parameters |
|-----------|-------------|------------|
| `bpm` | Set master BPM | beats per minute |
| `batch_update` | Atomic multi-parameter changes | list of updates |

**Batch Update Format:**
```python
performance_control('batch_update', updates=[
    {'type': 'layer_opacity', 'layer': 1, 'value': 0.8},
    {'type': 'clip_position', 'layer': 1, 'clip': 2, 'value': 0.5},
    {'type': 'effect_param', 'layer': 2, 'effect': 1, 'param': 1, 'value': 0.7}
])
```

**Natural Language Examples:**
- *"Set the BPM to 128"*
- *"Batch update: layer 1 to 60% opacity, layer 2 to screen blend mode"*

---

## 🎪 Live Performance Workflows

### Pre-Performance Setup

1. **Test Connection**
   ```
   Ask Claude: "Check Resolume connection status"
   ```

2. **Preload Clips**
   ```
   Ask Claude: "Load my main video files into different layers"
   ```

3. **Configure Layers**
   ```
   Ask Claude: "Set up layers with different blend modes and transitions"
   ```

4. **Set Performance Parameters**
   ```
   Ask Claude: "Set BPM to 120 for this techno set"
   ```

### During Performance

#### Basic Mixing
- **Layer Transitions**: *"Fade layer 2 in over 2 seconds"*
- **Clip Triggers**: *"Play the crowd shot on layer 1"*
- **Opacity Mixing**: *"Mix layer 1 at 70% and layer 2 at 80%"*

#### Effect Control
- **Parameter Automation**: *"Increase the distortion effect gradually"*
- **Effect Switching**: *"Switch to the kaleidoscope effect"*

#### Creative Techniques
- **Blend Mode Changes**: *"Switch to Multiply mode for a darker feel"*
- **Clip Positioning**: *"Scrub through the clip manually"*
- **Layer Bypassing**: *"Drop layer 3 for the breakdown"*

### Emergency Controls

- **Disable Problem Layer**: *"Bypass layer 2 immediately"*
- **Clear Stuck Clip**: *"Clear clip 1 from layer 1"*
- **Reset Opacity**: *"Set all layers to full opacity"*

---

## 🎵 BPM-Synced Effects

**Tempo-synchronized visual effects:**

1. **Set Master BPM**
   ```
   Ask Claude: "Set BPM to 140"
   ```

2. **Effect Parameters**
   ```
   Ask Claude: "Link effect speed to BPM"
   ```

3. **Real-time BPM Changes**
   ```
   Ask Claude: "Increase BPM to 160 for the drop"
   ```

---

## ⚡ Batch Operations

**Atomic parameter changes for smooth transitions:**

```python
# Complex scene transition
performance_control('batch_update', updates=[
    {'type': 'layer_opacity', 'layer': 1, 'value': 0.3},
    {'type': 'layer_opacity', 'layer': 2, 'value': 0.8},
    {'type': 'layer_opacity', 'layer': 3, 'value': 0.5},
    {'type': 'blend_mode', 'layer': 2, 'value': 1},  # Add mode
    {'type': 'effect_param', 'layer': 1, 'effect': 1, 'param': 1, 'value': 0.9}
])
```

**Natural Language:** *"Create a smooth transition with layer 1 at 30%, layer 2 at 80% with add blending, and boost the effect intensity"*

---

## 🎭 Performance Techniques

### Layer-Based Mixing

**Multi-layer compositions:**
- **Base Layer (1)**: Main content, Normal blend
- **Overlay (2)**: Effects/textures, Screen/Add blend
- **Key (3)**: Keyed elements, Normal blend
- **Effect (4)**: Global effects, Multiply blend

### Clip Sequencing

**Dynamic clip management:**
- **Preload Strategy**: Load clips before performance
- **Trigger System**: Quick clip switching
- **Position Control**: Manual scrubbing for builds

### Effect Automation

**Real-time parameter control:**
- **LFO Simulation**: Gradual parameter changes
- **Beat-synced**: BPM-linked effects
- **Manual Control**: Direct parameter manipulation

---

## 🔧 Troubleshooting

### Connection Issues

**"Not connected to Resolume"**
- ✅ Resolume Arena is running
- ✅ OSC enabled in Preferences
- ✅ Ports 7000/7001 not blocked
- ✅ Firewall allows local UDP traffic

**"Tool not responding"**
- Check Claude Desktop logs: `%APPDATA%\Claude\logs\`
- Verify MCP server is running
- Test with: `python -m resolume_mcp`

### Performance Issues

**"OSC messages not reaching Resolume"**
- Check Resolume OSC monitor
- Verify IP address (127.0.0.1)
- Test with smaller batch sizes

**"Effects not changing"**
- Confirm effect slot numbers (1-4 typical)
- Check parameter ranges (usually 0.0-1.0)
- Verify effect is enabled

---

## 🎯 Best Practices

### Preparation
- **Test Setup**: Always test connection before performance
- **Clip Organization**: Preload and organize clips logically
- **Parameter Ranges**: Know your effect parameter ranges
- **Blend Modes**: Understand blend mode characteristics

### Performance
- **Smooth Transitions**: Use transition durations for fades
- **Batch Operations**: Group related changes for atomic updates
- **Emergency Controls**: Know how to bypass/reset elements
- **Monitoring**: Use status checks during setup

### Creative Control
- **Layer Independence**: Each layer can have different timing
- **Blend Exploration**: Experiment with different blend modes
- **Effect Layering**: Combine multiple effects creatively
- **Parameter Mapping**: Map effects to performance energy

---

## 📚 Reference

### OSC Address Patterns

**Clips:**
```
/composition/layers/{layer}/clips/{clip}/connect
/composition/layers/{layer}/clips/{clip}/transport/position
/composition/layers/{layer}/clips/{clip}/video/opacity
```

**Layers:**
```
/composition/layers/{layer}/opacity
/composition/layers/{layer}/bypassed
/composition/layers/{layer}/blending/mode
/composition/layers/{layer}/transition/duration
```

**Effects:**
```
/composition/layers/{layer}/effects/{effect}/bypassed
/composition/layers/{layer}/effects/{effect}/params/{param}/value
```

**Global:**
```
/composition/tempomap/bpm
```

---

## 🎉 Ready for Performance!

With resolume-mcp, you can now control Resolume Arena using natural language commands. Focus on your creative vision while Claude handles the technical control!

**Happy VJing!** 🎬✨

---

*This guide is maintained as part of the resolume-mcp project.*





