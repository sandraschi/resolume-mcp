set windows-shell := ["powershell.exe", "-NoProfile", "-Command"]
import 'scripts/just/fleet.just'

# --- Dashboard ---

# Open the interactive recipe dashboard in the browser
default:
    @just --list

# --- Quality ---

# Execute Ruff SOTA v13.1 linting
lint:
    Set-Location '{{justfile_directory()}}'
    uv run ruff check .
    Set-Location '{{justfile_directory()}}\web_sota'
    npx @biomejs/biome ci .

# Execute Ruff SOTA v13.1 fix and formatting
fix:
    Set-Location '{{justfile_directory()}}'
    uv run ruff check . --fix --unsafe-fixes
    uv run ruff format .
    Set-Location '{{justfile_directory()}}\web_sota'
    npx @biomejs/biome check --write .

# --- Serve  Test ---

# Serve the MCP server
serve:
    Set-Location '{{justfile_directory()}}'
    uv run python -m resolume_mcp

# Run tests
test:
    Set-Location '{{justfile_directory()}}'
    uv run pytest tests/ -v

# Format Python code
fmt:
    Set-Location '{{justfile_directory()}}'
    uv run ruff format .

# TypeScript typecheck
types:
    Set-Location '{{justfile_directory()}}\web_sota'
    npx tsc --noEmit

# All gates green
gates-green: lint types
    Set-Location '{{justfile_directory()}}'
    uv run pytest tests/ -q

# --- Hardening ---

# Execute Bandit security audit
check-sec:
    Set-Location '{{justfile_directory()}}'
    uv run bandit -r src/

# Execute safety audit of dependencies
audit-deps:
    Set-Location '{{justfile_directory()}}'
    uv run safety check

# Bootstrap: install dev deps + pre-commit hook
bootstrap:
    uv sync --group dev
    uv run pre-commit install
    Write-Host "Pre-commit hooks installed." -ForegroundColor Green