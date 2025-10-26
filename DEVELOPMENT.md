# WheelX SDK Development Guide

This guide covers how to set up and develop the WheelX SDK and MCP server.

## Development Environment Setup

### Option 1: Using Nix + direnv (Recommended)

If you have Nix and direnv installed:

1. **Install Nix** (if not already installed):
   ```bash
   curl -L https://nixos.org/nix/install | sh
   ```

2. **Install direnv** and hook it to your shell:
   ```bash
   nix-env -i direnv
   # Add to your shell profile (.bashrc, .zshrc, etc.)
   echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
   ```

3. **Enter the development environment**:
   ```bash
   cd wheelx-sdk
   direnv allow
   ```

   This will automatically:
   - Create a Python virtual environment
   - Install all dependencies
   - Set up the development environment

### Option 2: Using Virtualenv Only

If you don't have Nix:

1. **Run the setup script**:
   ```bash
   ./setup_venv.sh
   ```

2. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

## Project Structure

```
wheelx-sdk/
├── python/                 # Python SDK and MCP server
│   ├── src/
│   │   └── wheelx_sdk/     # Core SDK package
│   ├── mcp_server.py       # MCP server implementation
│   ├── test_mcp_server.py  # Test script
│   ├── requirements-mcp.txt # MCP dependencies
│   └── setup.py            # SDK package setup
├── shell.nix              # Nix development shell
├── flake.nix              # Nix flake configuration
├── .envrc                 # direnv configuration
└── setup_venv.sh          # Virtualenv setup script
```

## MCP Server Development

### Running the MCP Server

1. **Ensure you're in the development environment** (Nix/direnv or virtualenv)

2. **Run the server**:
   ```bash
   cd python
   python mcp_server.py
   ```

   The server will start and show available tools and resources.

### Testing the MCP Server

Run the test script to verify functionality:

```bash
cd python
python test_mcp_server.py
```

### Available MCP Tools

- `get_quote` - Get swap/bridge quotes
- `get_order_status` - Check order status
- `get_supported_chains` - List supported networks
- `calculate_token_amount` - Convert human-readable amounts
- `estimate_gas_cost` - Estimate transaction costs
- `compare_quotes` - Compare quotes with different slippage

### Available MCP Resources

- `wheelx://chains/{chain_id}/tokens` - Get popular tokens for a chain
- `wheelx://status` - Service status
- `wheelx://docs/usage` - Usage documentation

## SDK Development

### Installing the SDK in Development Mode

The development environment automatically installs the SDK in development mode. This means changes to the SDK code are immediately available.

### Running SDK Tests

```bash
cd python
python -m pytest tests/  # If you have tests
```

### Code Quality

- **Formatting**: Use `black`
- **Linting**: Use `flake8`
- **Type checking**: Consider adding `mypy`

## Adding New Features

### Adding New MCP Tools

1. Add the tool function in `mcp_server.py`
2. Use the `@mcp.tool()` decorator
3. Add comprehensive docstring
4. Update the usage documentation

Example:
```python
@mcp.tool()
async def my_new_tool(param1: str, param2: int) -> Dict[str, Any]:
    """Description of what the tool does.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value
    """
    # Implementation here
    return {"result": "success"}
```

### Adding New MCP Resources

1. Add the resource function in `mcp_server.py`
2. Use the `@mcp.resource("uri://pattern")` decorator
3. Return string content (typically JSON or markdown)

Example:
```python
@mcp.resource("wheelx://data/{id}")
async def get_data(id: str) -> str:
    data = {"id": id, "value": "some data"}
    return json.dumps(data, indent=2)
```

## Deployment

### Building the SDK Package

```bash
cd python
python setup.py sdist bdist_wheel
```

### Publishing to PyPI

```bash
cd python
twine upload dist/*
```

## Troubleshooting

### Common Issues

1. **Virtual environment not activating**:
   - Run `source venv/bin/activate` manually
   - Check if `direnv allow` was run

2. **Import errors**:
   - Ensure `PYTHONPATH` includes `python/src`
   - Verify the SDK is installed in development mode

3. **MCP dependencies missing**:
   - Run `pip install -r python/requirements-mcp.txt`
   - Check if virtual environment is active

### Environment Variables

- `WHEELX_BASE_URL` - API base URL (default: https://wheelx.fi)
- `WHEELX_DEBUG` - Enable debug mode (default: false)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions:
- Create an issue in the repository
- Contact: dev@wheelx.fi