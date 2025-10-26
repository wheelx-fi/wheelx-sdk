#!/bin/bash

# Setup script for WheelX MCP Server

echo "Setting up WheelX MCP Server..."

# Install dependencies
echo "Installing dependencies..."
pip install fastmcp requests pydantic httpx uvicorn

# Test the installation
echo "Testing installation..."
python3 -c "import fastmcp; print('FastMCP installed successfully')"

# Run the test
echo "Running tests..."
python3 test_mcp_server.py

echo "Setup completed!"