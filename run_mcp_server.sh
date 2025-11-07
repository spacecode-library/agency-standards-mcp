#!/bin/bash
# Wrapper script to run MCP server with proper environment

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate virtual environment
source "$SCRIPT_DIR/.venv/bin/activate"

# Run the MCP server
exec python "$SCRIPT_DIR/src/agency_mcp_server.py"
