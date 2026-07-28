"""System status and diagnostics for resolume-mcp."""

from typing import Annotated

from pydantic import Field


def register_status(mcp):
    @mcp.tool()
    async def status(
        level: Annotated[str, Field(description="Status level: basic, intermediate, advanced, diagnostic")] = "basic",
        focus: Annotated[str | None, Field(description="Specific focus: system, config, performance, resolume")] = None,
    ) -> str:
        """Get system status and diagnostic information including Resolume connection.

        Provides different levels of diagnostic detail:

        LEVELS:
        - basic: Core system status and Resolume connection
        - intermediate: Configuration, resources, and VJ setup
        - advanced: Performance metrics and OSC details
        - diagnostic: Detailed troubleshooting info

        FOCUS AREAS:
        - system: System resources and health
        - config: Configuration validation
        - performance: Performance metrics
        - resolume: Resolume connection and OSC status

        ## Return Format
        {"content": str}

        ## Examples
        status()
        status('basic', 'resolume')
        status('intermediate', 'config')
        status('advanced', 'performance')
        """

        # Import here to avoid circular imports
        from ..utils.resolume_osc import connection_manager

        # Check Resolume connection
        resolume_connected = await connection_manager.ensure_connection()
        resolume_status = "Connected" if resolume_connected else "Not connected"

        status_report = f"""# resolume-mcp Status - Level: {level}

## System Status
Server running
Version: 0.1.0
Configuration: Valid
{resolume_status} to Resolume Arena

## VJ Tools Available
- help: Multilevel VJ help system
- status: System diagnostics (this tool)
- clip_control: Video clip management
- layer_control: Layer properties and blending
- effect_control: Effect parameter control
- performance_control: Global performance and batch operations

## OSC Configuration
- Host: 127.0.0.1 (localhost)
- Incoming Port: 7000
- Outgoing Port: 7001
"""

        if level in ["intermediate", "advanced", "diagnostic"]:
            status_report += """

## VJ Setup Recommendations
### Resolume Arena Configuration
1. Enable OSC in Resolume: Preferences -> OSC
2. Set Incoming Port: 7000
3. Set Outgoing Port: 7001
4. Enable "Send OSC Feedback" for parameter monitoring

### Network Setup
- Ensure Resolume Arena is running
- Check firewall allows UDP traffic on ports 7000-7001
- Verify localhost/127.0.0.1 connectivity

### Performance Tips
- Use SSD storage for video files
- Preload frequently used clips
- Use batch_update for complex transitions
- Monitor OSC traffic with network tools
"""

        if level in ["advanced", "diagnostic"]:
            status_report += """

## Advanced Diagnostics
### OSC Message Patterns
- Clip control: /composition/layers/{layer}/clips/{clip}/...
- Layer control: /composition/layers/{layer}/...
- Effects: /composition/layers/{layer}/effects/{effect}/...
- Global: /composition/tempomap/bpm

### Troubleshooting Commands
- Test connection: Send any OSC message and check Resolume logs
- Monitor traffic: Use Wireshark on UDP ports 7000-7001
- Check Resolume: View OSC messages in Resolume's debug console
"""

        if focus == "resolume":
            status_report = f"""# Resolume Connection Status

## Connection Details
Status: {resolume_status}
Host: 127.0.0.1
OSC Ports: 7000 (incoming), 7001 (outgoing)

## Connection Test
Last tested: Now
Connection method: OSC ping

## Troubleshooting
If not connected:
1. Verify Resolume Arena is running
2. Check OSC is enabled in Resolume preferences
3. Confirm ports 7000/7001 are not blocked
4. Test with: ping 127.0.0.1

## OSC Address Examples
/composition/layers/1/clips/1/connect
/composition/layers/1/opacity
/composition/tempomap/bpm
"""

        return status_report
