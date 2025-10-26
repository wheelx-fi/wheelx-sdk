{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "wheelx-sdk-dev";

  buildInputs = with pkgs; [
    python312
    python312Packages.pip
    python312Packages.virtualenv
    python312Packages.setuptools

    # Development tools
    direnv
    git

    # Optional: for web3 functionality
    # python312Packages.web3
  ];

  shellHook = ''
    # Set up Python virtual environment
    if [ ! -d "venv" ]; then
      echo "Creating Python virtual environment..."
      python -m venv venv
    fi

    # Activate virtual environment
    source venv/bin/activate

    # Install Python dependencies
    if [ -f "requirements-mcp.txt" ]; then
      echo "Installing MCP dependencies..."
      pip install -r requirements-mcp.txt
    fi

    # Install the wheelx-sdk package in development mode
    if [ -f "python/setup.py" ]; then
      echo "Installing wheelx-sdk in development mode..."
      cd python && pip install -e . && cd ..
    fi

    echo "Development environment ready!"
    echo "Virtual environment: venv/"
    echo "To activate manually: source venv/bin/activate"
  '';
}