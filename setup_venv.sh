#!/bin/bash

# Virtual environment setup script for WheelX SDK

set -e

echo "Setting up WheelX SDK virtual environment..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 not found. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install MCP dependencies
if [ -f "python/requirements-mcp.txt" ]; then
    echo "Installing MCP dependencies..."
    pip install -r python/requirements-mcp.txt
fi

# Install the SDK in development mode
if [ -f "python/setup.py" ]; then
    echo "Installing wheelx-sdk in development mode..."
    cd python && pip install -e . && cd ..
fi

echo ""
echo "Virtual environment setup complete!"
echo ""
echo "To activate the virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "To run the MCP server:"
echo "  cd python && python mcp_server.py"
echo ""
echo "To run tests:"
echo "  cd python && python test_mcp_server.py"