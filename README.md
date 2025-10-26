# WheelX SDK

Multi-language SDK for interacting with the WheelX quote API and executing token swap/bridge transactions.

## Overview

This repository contains SDK implementations in multiple programming languages for the WheelX quote API:

- **TypeScript SDK**: Complete implementation with ethers.js transaction execution (browser & Node.js)
- **Python SDK**: Complete implementation with web3 transaction execution
- **Go SDK**: Complete implementation with Ethereum transaction execution
- **MCP Server**: Model Context Protocol server for AI assistants and applications

## Quick Links

- [API Documentation](docs/QUOTE_ENDPOINT_DOCUMENTATION.md)
- [Project Overview](docs/PROJECT_OVERVIEW.md)
- [TypeScript SDK](typescript/README.md)
- [Python SDK](python/README.md)
- [Go SDK](go/README.md)

## Repository Structure

```
wheelx-sdk/
├── typescript/            # TypeScript SDK
│   ├── src/              # Source code
│   ├── examples/         # Usage examples
│   ├── tests/            # Test files
│   ├── package.json      # Package configuration
│   ├── tsconfig.json     # TypeScript configuration
│   └── README.md         # TypeScript SDK documentation
├── python/               # Python SDK
│   ├── src/wheelx_sdk/   # Source code
│   ├── examples/         # Usage examples
│   ├── mcp_server.py     # MCP server implementation
│   ├── setup.py          # Package configuration
│   ├── pyproject.toml    # Modern package config
│   └── README.md         # Python SDK documentation
├── go/                   # Go SDK
│   ├── pkg/wheelx/       # Source code
│   ├── examples/         # Usage examples
│   ├── go.mod            # Go module definition
│   └── README.md         # Go SDK documentation
├── docs/                 # Documentation
│   ├── QUOTE_ENDPOINT_DOCUMENTATION.md  # API reference
│   └── PROJECT_OVERVIEW.md              # Project overview
├── shell.nix             # Nix development shell
├── flake.nix             # Nix flake configuration
├── .envrc                # direnv configuration
├── setup_venv.sh         # Virtualenv setup script
├── DEVELOPMENT.md        # Development guide
└── README.md             # This file
```

## Features

### Common Features (All SDKs)

- **Quote Retrieval**: Get detailed swap/bridge quotes with pricing and transaction data
- **Cross-Chain Support**: Built-in support for multi-chain operations
- **Error Handling**: Comprehensive error handling for network and API errors
- **Type Safety**: Strong typing in all implementations
- **Documentation**: Complete API documentation with examples

### Language-Specific Features

#### TypeScript SDK
- Full TypeScript support with comprehensive type definitions
- `ethers.js` integration for transaction execution
- Browser and Node.js compatibility
- Modern ES modules and CommonJS support

#### Python SDK
- `dataclass` based models for type safety
- `requests` for HTTP communication
- Optional `web3.py` integration for transaction execution
- Async support ready

#### Go SDK
- Struct-based models with JSON tags
- `net/http` for HTTP communication
- `go-ethereum` integration for transaction execution
- Context-aware operations

#### MCP Server
- FastMCP-based server implementation
- Standardized tools and resources for AI assistants
- Cross-chain swap and bridge operations
- Real-time quote and order tracking

## Getting Started

### TypeScript

```bash
cd typescript
npm install
# See typescript/README.md for detailed usage
```

### Python

```bash
cd python
pip install -e .
# See python/README.md for detailed usage
```

### Go

```bash
cd go
go mod download
# See go/README.md for detailed usage
```

### MCP Server

```bash
# Using Nix + direnv (recommended)
direnv allow

# Or using virtualenv
./setup_venv.sh
source venv/bin/activate

# Run the server
cd python
python mcp_server.py
```

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed MCP server development setup.

## API Reference

See the [API Documentation](docs/QUOTE_ENDPOINT_DOCUMENTATION.md) for complete endpoint details, request/response schemas, and usage examples.

## Development

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Testing

Each SDK has its own testing approach:

- **TypeScript**: `jest`
- **Python**: `pytest`
- **Go**: `go test`

### Building

- **TypeScript**: `npm run build`
- **Python**: `python setup.py sdist bdist_wheel`
- **Go**: `go build ./pkg/wheelx`

## Security

- Never commit private keys or sensitive data
- Use environment variables for configuration
- Validate all transaction data before signing
- Use official RPC endpoints

## Support

- **API Issues**: Contact WheelX support
- **SDK Issues**: Open an issue in the respective SDK repository
- **Documentation**: Check the docs directory

## License

MIT License - see LICENSE file for details
