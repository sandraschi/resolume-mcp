"""VJ performance tools for Resolume control."""

import logging
from typing import Annotated, Literal

from pydantic import Field

from ..utils.resolume_osc import ResolumeConnectionManager

logger = logging.getLogger(__name__)

# Global connection manager
connection_manager = ResolumeConnectionManager()


def register_resource_tools(mcp):
    @mcp.tool()
    async def clip_control(
        operation: Annotated[
            Literal["load", "trigger", "clear", "position", "opacity"],
            Field(description="Clip control operation"),
        ],
        layer: Annotated[int, Field(description="Layer number (1-8 typically)")],
        clip: Annotated[int, Field(description="Clip slot number (1-10 typically)")],
        file_path: Annotated[str | None, Field(description="Full path to video file (for 'load' operation)")] = None,
        position: Annotated[float | None, Field(description="Playback position 0-1 (for 'position' op)")] = None,
        opacity: Annotated[float | None, Field(description="Opacity 0-1 (for 'opacity' op)")] = None,
    ) -> dict:
        """Control video clips in Resolume layers.

        CLIP OPERATIONS:
        - load: Load video file into clip slot
        - trigger: Start playback from beginning
        - clear: Remove clip from slot
        - position: Set playback position (0.0-1.0)
        - opacity: Set clip opacity (0.0-1.0)

        ## Return Format
        {"status": "success"|"error", "operation": str, "layer": int, "clip": int, "message": str}

        ## Examples
        clip_control('load', layer=1, clip=1, file_path='C:/videos/clip.mp4')
        clip_control('trigger', layer=1, clip=1)
        clip_control('position', layer=1, clip=1, position=0.5)
        clip_control('opacity', layer=1, clip=1, opacity=0.5)
        clip_control('clear', layer=1, clip=1)
        """
        try:
            client = await connection_manager.get_client()

            if operation == "load":
                if not file_path:
                    return {"status": "error", "message": "file_path required for load operation"}
                await client.load_clip(layer, clip, file_path)
                message = f"Loaded {file_path} into layer {layer}, clip {clip}"

            elif operation == "trigger":
                await client.trigger_clip(layer, clip)
                message = f"Triggered playback for layer {layer}, clip {clip}"

            elif operation == "clear":
                await client.clear_clip(layer, clip)
                message = f"Cleared clip from layer {layer}, clip {clip}"

            elif operation == "position":
                if position is None:
                    return {"status": "error", "message": "position required for position operation"}
                await client.set_clip_position(layer, clip, position)
                message = f"Set clip {clip} position to {position:.2f}"

            elif operation == "opacity":
                if opacity is None:
                    return {"status": "error", "message": "opacity required for opacity operation"}
                await client.set_clip_opacity(layer, clip, opacity)
                message = f"Set clip {clip} opacity to {opacity:.2f}"

            return {"status": "success", "operation": operation, "layer": layer, "clip": clip, "message": message}

        except Exception as e:
            logger.error(f"Clip control failed: {e}")
            return {"status": "error", "message": str(e)}

    @mcp.tool()
    async def layer_control(
        operation: Annotated[
            Literal["opacity", "bypass", "blend_mode", "transition"],
            Field(description="Layer control operation"),
        ],
        layer: Annotated[int, Field(description="Layer number (1-8 typically)")],
        value: Annotated[float | None, Field(description="Opacity 0.0-1.0 or transition time in seconds")] = None,
        enabled: Annotated[bool | None, Field(description="Boolean for bypass operation")] = None,
        blend_mode: Annotated[int | None, Field(description="Blend mode number (0-11)")] = None,
    ) -> dict:
        """Control layer properties in Resolume composition.

        LAYER OPERATIONS:
        - opacity: Set layer opacity (0.0-1.0)
        - bypass: Enable/disable layer
        - blend_mode: Set blending mode (0-11)
        - transition: Set transition duration in seconds

        BLEND MODES:
        0: Normal, 1: Add, 2: Subtract, 3: Multiply, 4: Screen,
        5: Overlay, 6: Hard Light, 7: Soft Light, 8: Color Dodge,
        9: Color Burn, 10: Darken, 11: Lighten

        ## Return Format
        {"status": "success"|"error", "operation": str, "layer": int, "message": str}

        ## Examples
        layer_control('opacity', layer=1, value=0.75)
        layer_control('bypass', layer=2, enabled=False)
        layer_control('blend_mode', layer=1, blend_mode=1)
        layer_control('transition', layer=1, value=2.0)
        """
        try:
            client = await connection_manager.get_client()

            if operation == "opacity":
                if value is None:
                    return {"status": "error", "message": "value required for opacity operation"}
                await client.set_layer_opacity(layer, value)
                message = f"Layer {layer} opacity set to {value:.2f}"

            elif operation == "bypass":
                if enabled is None:
                    return {"status": "error", "message": "enabled required for bypass operation"}
                await client.set_layer_bypass(layer, not enabled)
                message = f"Layer {layer} {'enabled' if enabled else 'disabled'}"

            elif operation == "blend_mode":
                if blend_mode is None:
                    return {"status": "error", "message": "blend_mode required for blend_mode operation"}
                await client.set_blend_mode(layer, blend_mode)
                message = f"Layer {layer} blend mode set to {blend_mode}"

            elif operation == "transition":
                if value is None:
                    return {"status": "error", "message": "value required for transition operation"}
                await client.set_layer_transition(layer, value)
                message = f"Layer {layer} transition set to {value:.1f}s"

            return {"status": "success", "operation": operation, "layer": layer, "message": message}

        except Exception as e:
            logger.error(f"Layer control failed: {e}")
            return {"status": "error", "message": str(e)}

    @mcp.tool()
    async def effect_control(
        operation: Annotated[Literal["parameter", "bypass"], Field(description="Effect control operation")],
        layer: Annotated[int, Field(description="Layer number (1-8 typically)")],
        effect: Annotated[int, Field(description="Effect slot number (1-4 typically)")],
        parameter: Annotated[int | None, Field(description="Parameter number (1-based, for 'parameter' op)")] = None,
        value: Annotated[float | None, Field(description="Parameter value 0-1 (for 'parameter' op)")] = None,
        enabled: Annotated[bool | None, Field(description="Boolean for bypass operation")] = None,
    ) -> dict:
        """Control effects on Resolume layers.

        EFFECT OPERATIONS:
        - parameter: Set effect parameter value (0.0-1.0)
        - bypass: Enable/disable effect

        ## Return Format
        {"status": "success"|"error", "operation": str, "layer": int, "effect": int, "message": str}

        ## Examples
        effect_control('parameter', layer=1, effect=1, parameter=1, value=0.8)
        effect_control('bypass', layer=2, effect=1, enabled=False)
        """
        try:
            client = await connection_manager.get_client()

            if operation == "parameter":
                if parameter is None or value is None:
                    return {"status": "error", "message": "parameter and value required for parameter operation"}
                await client.set_effect_parameter(layer, effect, parameter, value)
                message = f"Layer {layer} effect {effect} parameter {parameter} set to {value:.2f}"

            elif operation == "bypass":
                if enabled is None:
                    return {"status": "error", "message": "enabled required for bypass operation"}
                await client.bypass_effect(layer, effect, not enabled)
                message = f"Layer {layer} effect {effect} {'enabled' if enabled else 'disabled'}"

            return {"status": "success", "operation": operation, "layer": layer, "effect": effect, "message": message}

        except Exception as e:
            logger.error(f"Effect control failed: {e}")
            return {"status": "error", "message": str(e)}

    @mcp.tool()
    async def performance_control(
        operation: Annotated[Literal["bpm", "batch_update"], Field(description="Performance control operation")],
        bpm: Annotated[float | None, Field(description="Beats per minute (60-200, for 'bpm' operation)")] = None,
        updates: Annotated[list | None, Field(description="List of update commands (for 'batch_update')")] = None,
    ) -> dict:
        """Control global performance parameters and batch operations.

        PERFORMANCE OPERATIONS:
        - bpm: Set master BPM for tempo-synced effects
        - batch_update: Execute multiple parameter changes atomically

        ## Return Format
        {"status": "success"|"error", "operation": str, "message": str}

        ## Examples
        performance_control('bpm', bpm=128.0)
        performance_control('batch_update', updates=[
            {'type': 'layer_opacity', 'layer': 1, 'value': 0.8},
            {'type': 'clip_position', 'layer': 1, 'clip': 2, 'value': 0.5},
            {'type': 'effect_param', 'layer': 2, 'effect': 1, 'param': 1, 'value': 0.7}
        ])
        """
        try:
            client = await connection_manager.get_client()

            if operation == "bpm":
                if bpm is None:
                    return {"status": "error", "message": "bpm required for bpm operation"}
                await client.set_master_bpm(bpm)
                message = f"Master BPM set to {bpm}"

            elif operation == "batch_update":
                if not updates:
                    return {"status": "error", "message": "updates required for batch_update operation"}

                osc_messages = []

                for update in updates:
                    update_type = update.get("type")
                    if update_type == "layer_opacity":
                        address = f"/composition/layers/{update['layer']}/opacity"
                        osc_messages.append((address, update["value"]))
                    elif update_type == "clip_position":
                        address = f"/composition/layers/{update['layer']}/clips/{update['clip']}/transport/position"
                        osc_messages.append((address, update["value"]))
                    elif update_type == "clip_opacity":
                        address = f"/composition/layers/{update['layer']}/clips/{update['clip']}/video/opacity"
                        osc_messages.append((address, update["value"]))
                    elif update_type == "effect_param":
                        address = f"/composition/layers/{update['layer']}/effects/{update['effect']}/params/{update['param']}/value"
                        osc_messages.append((address, update["value"]))

                if osc_messages:
                    await client.send_bundle(osc_messages)
                    message = f"Executed batch update with {len(osc_messages)} changes"
                else:
                    return {"status": "error", "message": "No valid updates in batch"}

            return {"status": "success", "operation": operation, "message": message}

        except Exception as e:
            logger.error(f"Performance control failed: {e}")
            return {"status": "error", "message": str(e)}
