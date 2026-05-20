# resolume-mcp

<p align="center">
  <a href="https://github.com/casey/just"><img src="https://img.shields.io/badge/just-ready_to_go-7c5cfc?style=flat-square&logo=just&logoColor=white" alt="Just"></a>
  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.13+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://github.com/PrefectHQ/fastmcp"><img src="https://img.shields.io/badge/FastMCP-3.2-7c5cfc?style=flat-square" alt="FastMCP"></a>
</p>


> 📖 **[Installation Guide](INSTALL.md)** — quick start, manual setup, and troubleshooting

**MCP server for Resolume Arena VJ software control and automation - Live video mixing from natural language commands**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.12%2B-green.svg)](https://github.com/jlowin/fastmcp)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Resolume](https://img.shields.io/badge/Resolume-Arena-orange.svg)](https://resolume.com/)

---

## Quick Start

```powershell
git clone https://github.com/sandraschi/resolume-mcp
cd resolume-mcp
just
```

This opens an interactive dashboard showing all available commands. Run `just bootstrap` to install dependencies, then `just serve` or `just dev` to start.

### Manual Setup

If you don't have `just` installed:

##  Features

-  **Real-time Clip Control** - Load, trigger, position, and opacity control for video clips
-  **Layer Management** - Opacity, blending modes, transitions, and bypass control
-  **Effect Automation** - Parameter control and effect bypassing for visual effects
-  **Performance Tools** - BPM synchronization and atomic batch operations
-  **OSC Integration** - Direct communication with Resolume Arena via OSC protocol
-  **Live VJ Support** - Optimized for live video performances and real-time mixing

---

## Resolume Arena (host app): demo vs license

**Resolume Arena** is not included in this repoit is the VJ application you control via OSC.

There is **no** separate perpetual free tier. Resolume provides **fully functional demos** (Avenue and Arena) from the [official download page](https://resolume.com/download/): you may use them **as long as you like**; the main limits are a **watermark on output** and **voice reminders** until you purchase a license. See Resolumes [Difference between Avenue and Arena](https://resolume.com/support/en/avenue-arena-difference) (section Demo).

More detail: [docs/user-guide/RESOLUME_ARENA_DEMO_AND_LICENSING.md](docs/user-guide/RESOLUME_ARENA_DEMO_AND_LICENSING.md).

---

##  Installation

### Prerequisites
- [uv](https://docs.astral.sh/uv/) installed (RECOMMENDED)
- Python 3.12+

###  Quick Start
Run immediately via `uvx`:
```bash
uvx resolume-mcp
```

###  Claude Desktop Integration
Add to your `claude_desktop_config.json`:
```json
"mcpServers": {
  "resolume-mcp": {
    "command": "uv",
    "args": ["--directory", "D:/Dev/repos/resolume-mcp", "run", "resolume-mcp"]
  }
}
```
### Prerequisites

- Python 3.10 or higher
- Resolume Arena (or Arena) installed and running
- OSC enabled in Resolume preferences (ports 7000/7001)
- Claude Desktop for MCP integration

### Install via MCPB (Recommended)

1. Download the latest `.mcpb` package from [Releases](https://github.com/sandr/resolume-mcp/releases)
2. Drag the `.mcpb` file to Claude Desktop
3. Configure settings (see [Configuration](#configuration))
4. Restart Claude Desktop

### Install from Source

```bash
# Clone repository
git clone https://github.com/sandr/resolume-mcp.git
cd resolume-mcp

# Install with pip
pip install -e .
```

---

##  Quick Start

### Claude Desktop Configuration

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

**Resolume Setup:**
1. Open Resolume Arena  **Preferences**  **OSC**
2. Enable OSC: 
3. **Incoming Port**: 7000
4. **Outgoing Port**: 7001

### First Steps

```bash
# Test the installation
Ask Claude: "What resolume-mcp tools are available?"

# Check Resolume connection
Ask Claude: "Check Resolume connection status"

# Load your first clip
Ask Claude: "Load C:/videos/my_clip.mp4 into layer 1, clip 1"
```

---

##  Configuration

### Resolume OSC Setup

**Required Configuration in Resolume Arena:**

1. **Enable OSC**: Preferences  OSC  Enable OSC
2. **Ports**:
   - Incoming Port: `7000`
   - Outgoing Port: `7001`
3. **IP Address**: `127.0.0.1` (localhost)
4. **Send Feedback**: Optional (enables parameter monitoring)

### Network Requirements

- Resolume Arena must be running
- UDP ports 7000-7001 must be available
- Localhost connectivity required
- No firewall blocking required for local communication

### Advanced Configuration

See [docs/user-guide/](docs/user-guide/) for detailed setup guides.

---

##  Documentation

| Document | Description |
|----------|-------------|
| [Resolume demo & licensing](docs/user-guide/RESOLUME_ARENA_DEMO_AND_LICENSING.md) | Official demo mode (watermark), Avenue vs Arena, links |
| [Integration Guide](docs/integration-guide.md) | Setup with Claude Desktop |
| [Architecture](docs/architecture.md) | System design and components |
| [Tool Reference](docs/tools-reference.md) | Complete API documentation |
| [Examples](docs/examples/) | Working examples |
| [Troubleshooting](docs/troubleshooting.md) | Common issues and solutions |

---

##  Usage Examples

### Basic VJ Operations

```bash
# Load video clips
Ask Claude: "Load my_clip.mp4 into layer 1, clip 1"

# Control playback
Ask Claude: "Trigger clip 1 on layer 1"

# Mix layers
Ask Claude: "Set layer 2 opacity to 70%"

# Apply effects
Ask Claude: "Set effect parameter 1 on layer 1, effect 1 to 0.8"
```

### Live Performance Workflow

```bash
# Pre-performance setup
Ask Claude: "Set master BPM to 128"

# During performance
Ask Claude: "Fade layer 1 to 50% opacity over 2 seconds"
Ask Claude: "Switch to Add blend mode on layer 2"
Ask Claude: "Batch update: layer 1 opacity 0.3, layer 2 opacity 0.7, effect 1 param 1 to 0.9"
```

### Advanced Examples

See [docs/user-guide/](docs/user-guide/) for complete VJ workflow examples.

---

##  Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/sandr/resolume-mcp.git
cd resolume-mcp

# Install development dependencies
uv sync --dev

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov

# Run specific test
uv run pytest tests/test_specific.py -v
```

### Code Quality

```bash
# Lint with ruff
uv run ruff check .

# Format with ruff
uv run ruff format .

# Type check
uv run mypy .
```

---

##  Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/-feature`)
3. Make your changes
4. Run tests and linters
5. Commit your changes (`git commit -m 'Add  feature'`)
6. Push to the branch (`git push origin feature/-feature`)
7. Open a Pull Request

---

##  Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.

---


## 🛡️ Industrial Quality Stack

This project adheres to **SOTA 14.1** industrial standards for high-fidelity agentic orchestration:

- **Python (Core)**: [Ruff](https://astral.sh/ruff) for linting and formatting. Zero-tolerance for `print` statements in core handlers (`T201`).
- **Webapp (UI)**: [Biome](https://biomejs.dev/) for sub-millisecond linting. Strict `noConsoleLog` enforcement.
- **Protocol Compliance**: Hardened `stdout/stderr` isolation to ensure crash-resistant JSON-RPC communication.
- **Automation**: [Justfile](./justfile) recipes for all fleet operations (`just lint`, `just fix`, `just dev`).
- **Security**: Automated audits via `bandit` and `safety`.

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

##  Acknowledgments

- [FastMCP](https://github.com/jlowin/fastmcp) - Modern MCP server framework
- [Claude Desktop](https://claude.ai/desktop) - AI assistant platform
- {Other acknowledgments}

---

##  Support

- **Issues:** [GitHub Issues](https://github.com/sandr/resolume-mcp/issues)
- **Discussions:** [GitHub Discussions](https://github.com/sandr/resolume-mcp/discussions)
- **Email:** your-email@example.com

---

**Status:** Beta - Ready for live VJ performances  
**MCP Version:** FastMCP 3.1.0+  
**Maintained by:** Sandra Schipal  
**Last Updated:** 2025-12-24
