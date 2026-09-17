# resolume-mcp — Agent Instructions

FastMCP 3.4 Resolume Arena VJ control server via OSC.

## Quick Start
uv run python -m resolume_mcp

## Key Files
- src/resolume_mcp/__main__.py — FastMCP server entry point
- src/resolume_mcp/tools/ — 6 tools: help, status, clip/layer/effect/performance control
- src/resolume_mcp/utils/resolume_osc.py — OSC communication layer
- web_sota/ — React frontend (Vite, :11139)
- native/ — Tauri 2.0 NSIS desktop wrapper

## Commands
just lint          # ruff + biome
just test          # pytest
just fmt           # ruff format
