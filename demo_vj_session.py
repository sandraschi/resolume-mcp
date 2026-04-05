#!/usr/bin/env python3
"""
Demo VJ Session - Resolume MCP Live Performance Simulation

This script demonstrates a complete VJ performance workflow using the resolume-mcp tools.
Run this with Resolume Arena open to see real-time control in action.

Usage:
    python demo_vj_session.py

Make sure Resolume Arena is running with OSC enabled (ports 7000/7001).
"""

import asyncio
import time
from resolume_mcp.utils.resolume_osc import ResolumeConnectionManager

async def demo_vj_performance():
    """Demonstrate a complete VJ performance workflow."""

    print("🎬 Resolume MCP - Live VJ Performance Demo")
    print("=" * 50)

    # Initialize connection
    connection_manager = ResolumeConnectionManager()

    # Test connection
    print("🔗 Testing connection to Resolume...")
    connected = await connection_manager.ensure_connection()

    if not connected:
        print("❌ Could not connect to Resolume. Please ensure:")
        print("   - Resolume Arena is running")
        print("   - OSC is enabled in Preferences")
        print("   - Ports 7000/7001 are available")
        return

    print("✅ Connected to Resolume Arena!")
    client = await connection_manager.get_client()

    # Performance sequence
    print("\n🎭 Starting VJ Performance Sequence...")

    # 1. Preload clips (simulate loading video files)
    print("\n📼 Preloading clips...")
    # Note: In real usage, replace with actual video file paths
    print("   (Demo mode - no actual files loaded)")

    # 2. Set initial performance parameters
    print("\n🎵 Setting performance parameters...")
    await client.set_master_bpm(128.0)
    print("   BPM set to 128")

    # 3. Configure layers
    print("\n🎛️ Configuring layers...")

    # Layer 1: Base layer with normal blend
    await client.set_layer_opacity(1, 1.0)
    await client.set_blend_mode(1, 0)  # Normal
    await client.set_layer_transition(1, 1.0)
    print("   Layer 1: Full opacity, Normal blend, 1s transitions")

    # Layer 2: Overlay layer with Add blend
    await client.set_layer_opacity(2, 0.0)  # Start invisible
    await client.set_blend_mode(2, 1)  # Add
    await client.set_layer_transition(2, 2.0)
    print("   Layer 2: Zero opacity, Add blend, 2s transitions")

    # 4. Simulate live performance
    print("\n🎪 Live Performance Sequence:")

    # Beat 1-4: Build up with layer 1
    print("\n   Beats 1-4: Building with Layer 1")
    await asyncio.sleep(1)  # Simulate timing

    # Beat 5-8: Bring in layer 2
    print("   Beats 5-8: Introducing Layer 2")
    await client.set_layer_opacity(2, 0.3)
    await asyncio.sleep(1)

    # Beat 9-12: Mix both layers
    print("   Beats 9-12: Mixing both layers")
    await client.set_layer_opacity(1, 0.7)
    await client.set_layer_opacity(2, 0.6)
    await asyncio.sleep(1)

    # Beat 13-16: Effect modulation
    print("   Beats 13-16: Effect modulation")
    # Simulate effect parameter changes
    print("   (Effect parameters would modulate here)")
    await asyncio.sleep(1)

    # Climax: Full mix
    print("   Climax: Full layer mix")
    await client.set_layer_opacity(1, 0.8)
    await client.set_layer_opacity(2, 0.9)
    await asyncio.sleep(1)

    # Wind down
    print("   Wind down: Fading layers")
    await client.set_layer_opacity(2, 0.3)
    await asyncio.sleep(0.5)
    await client.set_layer_opacity(2, 0.0)
    await asyncio.sleep(0.5)
    await client.set_layer_opacity(1, 0.5)
    await asyncio.sleep(0.5)
    await client.set_layer_opacity(1, 0.0)

    print("\n🎉 Performance complete!")

    # 5. Batch operation demo
    print("\n⚡ Demonstrating batch operations...")

    # Prepare batch update
    batch_updates = [
        {'type': 'layer_opacity', 'layer': 1, 'value': 0.5},
        {'type': 'layer_opacity', 'layer': 2, 'value': 0.5},
        {'type': 'blend_mode', 'layer': 1, 'value': 4},  # Screen mode
        {'type': 'blend_mode', 'layer': 2, 'value': 3},  # Multiply mode
    ]

    print(f"   Executing {len(batch_updates)} operations atomically...")
    await client.send_bundle([
        ('/composition/layers/1/opacity', 0.5),
        ('/composition/layers/2/opacity', 0.5),
        ('/composition/layers/1/blending/mode', 4),
        ('/composition/layers/2/blending/mode', 3),
    ])
    print("   ✅ Batch update completed")

    print("\n📊 Demo Summary:")
    print("   ✅ OSC Connection established")
    print("   ✅ Layer control (opacity, blending, transitions)")
    print("   ✅ Performance parameters (BPM)")
    print("   ✅ Batch operations")
    print("   ✅ Real-time parameter changes")

    print("\n🔧 Available Tools in Claude:")
    print("   - clip_control: Load, trigger, position, opacity")
    print("   - layer_control: Opacity, blending, transitions")
    print("   - effect_control: Parameter automation, bypassing")
    print("   - performance_control: BPM sync, batch operations")
    print("   - status: Connection monitoring")
    print("   - help: VJ-specific assistance")

    print("\n🎬 Ready for live VJ performances!")
    print("   Use Claude Desktop to control Resolume with natural language!")

if __name__ == "__main__":
    asyncio.run(demo_vj_performance())





