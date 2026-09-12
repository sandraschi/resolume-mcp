"""OSC communication utilities for Resolume control.

This module provides OSC client functionality for communicating with Resolume Arena.
Resolume uses OSC (Open Sound Control) for external control and automation.

OSC Address Space Reference:
- /composition/layers/{layer}/clips/{clip}/connect -> Load clip
- /composition/layers/{layer}/clips/{clip}/transport/position -> Clip position (0-1)
- /composition/layers/{layer}/clips/{clip}/video/opacity -> Clip opacity (0-1)
- /composition/layers/{layer}/opacity -> Layer opacity (0-1)
- /composition/layers/{layer}/bypassed -> Layer bypass (0/1)
- /composition/layers/{layer}/blending/mode -> Blend mode (0-11)
- /composition/layers/{layer}/effects/{effect}/bypassed -> Effect bypass
- /composition/layers/{layer}/effects/{effect}/params/{param} -> Effect parameters

Default Resolume OSC settings:
- Incoming: Port 7000
- Outgoing: Port 7001
- IP: 127.0.0.1 (localhost)
"""

import asyncio
import logging

from pythonosc import udp_client
from pythonosc.osc_bundle import OscBundle
from pythonosc.osc_message import OscMessage

logger = logging.getLogger(__name__)


class ResolumeOSCClient:
    """OSC client for controlling Resolume Arena.

    Provides high-level methods for common VJ operations while maintaining
    low-level OSC message sending capabilities.
    """

    def __init__(self, host: str = "127.0.0.1", incoming_port: int = 7000, outgoing_port: int = 7001):
        """Initialize OSC client for Resolume communication.

        Args:
            host: IP address of Resolume machine (default: localhost)
            incoming_port: Port Resolume listens on (default: 7000)
            outgoing_port: Port to send messages to Resolume (default: 7001)
        """
        self.host = host
        self.incoming_port = incoming_port
        self.outgoing_port = outgoing_port

        # Commands go to Resolume's *incoming* port (Preferences > OSC > Incoming).
        self.client = udp_client.SimpleUDPClient(host, incoming_port)

        # Connection status
        self.connected = False

        logger.info(f"Initialized Resolume OSC client: {host}:{outgoing_port}")

    async def connect(self) -> bool:
        """Test connection to Resolume by sending a ping message.

        Returns:
            True if connection successful, False otherwise
        """
        try:
            # Send a harmless OSC message to test connection
            # /ping is not a standard Resolume command, but we can use it to test
            await self.send_message("/ping", 1)
            self.connected = True
            logger.info("Successfully connected to Resolume")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Resolume: {e}")
            self.connected = False
            return False

    async def send_message(self, address: str, *args: int | float | str | bytes | bool) -> None:
        """Send OSC message to Resolume.

        Args:
            address: OSC address (e.g., '/composition/layers/1/opacity')
            *args: OSC arguments (numbers, strings, etc.)
        """
        try:
            self.client.send_message(address, args)
            logger.debug(f"Sent OSC: {address} {args}")
        except Exception as e:
            logger.error(f"Failed to send OSC message {address}: {e}")
            raise

    async def send_bundle(self, messages: list) -> None:
        """Send multiple OSC messages as a bundle for atomic updates.

        Args:
            messages: List of (address, args) tuples
        """
        try:
            bundle = OscBundle()
            for address, args in messages:
                msg = OscMessage(address, args)
                bundle.append(msg)

            self.client.send(bundle)
            logger.debug(f"Sent OSC bundle with {len(messages)} messages")
        except Exception as e:
            logger.error(f"Failed to send OSC bundle: {e}")
            raise

    # High-level VJ control methods

    async def load_clip(self, layer: int, clip: int, clip_path: str) -> None:
        """Load a video clip into a specific layer and clip slot.

        Args:
            layer: Layer number (1-based)
            clip: Clip slot number (1-based)
            clip_path: Full path to video file
        """
        address = f"/composition/layers/{layer}/clips/{clip}/connect"
        await self.send_message(address, clip_path)

    async def set_clip_position(self, layer: int, clip: int, position: float) -> None:
        """Set playback position of a clip (0.0 to 1.0).

        Args:
            layer: Layer number (1-based)
            clip: Clip slot number (1-based)
            position: Position from 0.0 (start) to 1.0 (end)
        """
        address = f"/composition/layers/{layer}/clips/{clip}/transport/position"
        await self.send_message(address, max(0.0, min(1.0, position)))

    async def set_clip_opacity(self, layer: int, clip: int, opacity: float) -> None:
        """Set opacity of a clip (0.0 to 1.0).

        Args:
            layer: Layer number (1-based)
            clip: Clip slot number (1-based)
            opacity: Opacity from 0.0 (transparent) to 1.0 (opaque)
        """
        address = f"/composition/layers/{layer}/clips/{clip}/video/opacity"
        await self.send_message(address, max(0.0, min(1.0, opacity)))

    async def set_layer_opacity(self, layer: int, opacity: float) -> None:
        """Set opacity of a layer (0.0 to 1.0).

        Args:
            layer: Layer number (1-based)
            opacity: Opacity from 0.0 (transparent) to 1.0 (opaque)
        """
        address = f"/composition/layers/{layer}/opacity"
        await self.send_message(address, max(0.0, min(1.0, opacity)))

    async def set_layer_bypass(self, layer: int, bypassed: bool) -> None:
        """Enable or disable a layer.

        Args:
            layer: Layer number (1-based)
            bypassed: True to bypass (disable), False to enable
        """
        address = f"/composition/layers/{layer}/bypassed"
        await self.send_message(address, 1 if bypassed else 0)

    async def set_blend_mode(self, layer: int, mode: int) -> None:
        """Set blending mode for a layer.

        Args:
            layer: Layer number (1-based)
            mode: Blend mode (0-11):
                0: Normal, 1: Add, 2: Subtract, 3: Multiply, 4: Screen,
                5: Overlay, 6: Hard Light, 7: Soft Light, 8: Color Dodge,
                9: Color Burn, 10: Darken, 11: Lighten
        """
        address = f"/composition/layers/{layer}/blending/mode"
        await self.send_message(address, max(0, min(11, mode)))

    async def set_effect_parameter(self, layer: int, effect: int, parameter: int, value: float) -> None:
        """Set parameter value for an effect on a layer.

        Args:
            layer: Layer number (1-based)
            effect: Effect slot number (1-based)
            parameter: Parameter number (1-based)
            value: Parameter value (typically 0.0 to 1.0)
        """
        address = f"/composition/layers/{layer}/effects/{effect}/params/{parameter}/value"
        await self.send_message(address, max(0.0, min(1.0, value)))

    async def bypass_effect(self, layer: int, effect: int, bypassed: bool) -> None:
        """Enable or disable an effect on a layer.

        Args:
            layer: Layer number (1-based)
            effect: Effect slot number (1-based)
            bypassed: True to bypass (disable), False to enable
        """
        address = f"/composition/layers/{layer}/effects/{effect}/bypassed"
        await self.send_message(address, 1 if bypassed else 0)

    async def trigger_clip(self, layer: int, clip: int) -> None:
        """Trigger playback of a clip (play from beginning).

        Args:
            layer: Layer number (1-based)
            clip: Clip slot number (1-based)
        """
        address = f"/composition/layers/{layer}/clips/{clip}/connect"
        await self.send_message(address, 1)

    async def clear_clip(self, layer: int, clip: int) -> None:
        """Clear a clip slot.

        Args:
            layer: Layer number (1-based)
            clip: Clip slot number (1-based)
        """
        address = f"/composition/layers/{layer}/clips/{clip}/clear"
        await self.send_message(address, 1)

    async def set_master_bpm(self, bpm: float) -> None:
        """Set the master BPM for tempo-synced effects.

        Args:
            bpm: Beats per minute (typically 60-200)
        """
        address = "/composition/tempomap/bpm"
        await self.send_message(address, max(1, min(300, bpm)))

    async def set_layer_transition(self, layer: int, transition_time: float) -> None:
        """Set transition time for layer changes.

        Args:
            layer: Layer number (1-based)
            transition_time: Transition time in seconds
        """
        address = f"/composition/layers/{layer}/transition/duration"
        await self.send_message(address, max(0.0, transition_time))


class ResolumeConnectionManager:
    """Manages Resolume OSC connection and provides error handling."""

    def __init__(self, host: str = "127.0.0.1", port: int = 7000):
        self.client: ResolumeOSCClient | None = None
        self.host = host
        self.port = port
        self._connection_lock = asyncio.Lock()

    async def get_client(self) -> ResolumeOSCClient:
        """Get or create OSC client with lazy initialization."""
        async with self._connection_lock:
            if self.client is None:
                self.client = ResolumeOSCClient(self.host, incoming_port=self.port)

            if not self.client.connected:
                await self.client.connect()

            return self.client

    async def ensure_connection(self) -> bool:
        """Ensure Resolume connection is active.

        Returns:
            True if connected, False otherwise
        """
        try:
            client = await self.get_client()
            return client.connected
        except Exception:
            return False

    async def disconnect(self) -> None:
        """Clean up OSC connection."""
        if self.client:
            # OSC client doesn't have explicit disconnect method
            # Just mark as disconnected
            self.client.connected = False
            self.client = None
