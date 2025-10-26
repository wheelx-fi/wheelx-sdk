{
  description = "WheelX SDK Development Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          name = "wheelx-sdk";

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
            if [ -f "python/requirements-mcp.txt" ]; then
              echo "Installing MCP dependencies..."
              pip install -r python/requirements-mcp.txt
            fi

            # Install the wheelx-sdk package in development mode
            if [ -f "python/setup.py" ]; then
              echo "Installing wheelx-sdk in development mode..."
              cd python && pip install -e . && cd ..
            fi

            echo "WheelX SDK development environment ready!"
            echo "Virtual environment: venv/"
            echo "To activate manually: source venv/bin/activate"
          '';
        };

        # Optional: Define packages if you want to build the SDK
        packages.default = pkgs.python312Packages.buildPythonPackage {
          pname = "wheelx-sdk";
          version = "0.1.0";
          src = ./python;
          propagatedBuildInputs = with pkgs.python312Packages; [
            requests
          ];
        };
      }
    );
}