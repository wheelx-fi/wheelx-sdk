# WheelX MCP Server

A Model Context Protocol (MCP) server for WheelX DeFi swap and bridge operations, built with Python and FastMCP.

## Features

### Tools
- **get_quote**: Get quotes for token swaps and cross-chain bridges
- **get_order_status**: Check the status of submitted orders
- **get_supported_chains**: Get list of supported blockchain networks
- **calculate_token_amount**: Convert human-readable amounts to raw token amounts
- **estimate_gas_cost**: Estimate gas costs for transactions
- **compare_quotes**: Compare quotes with different slippage settings

### Resources
- **wheelx://chains/{chain_id}/tokens**: Get popular tokens for specific chains
- **wheelx://status**: Check service status and availability
- **wheelx://docs/usage**: Usage documentation

## Installation

1. Install dependencies:
```bash
pip install fastmcp requests
```

2. Run the server:
```bash
python mcp_server.py
```

## Usage Examples

### Getting a Quote
```python
# Get a quote for swapping USDC to USDT on Ethereum
quote = await get_quote(
    from_chain=1,
    to_chain=1,
    from_token="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    to_token="0xdAC17F958D2ee523a2206206994597C13D831ec7",
    from_address="0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
    to_address="0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
    amount=1000000,
    slippage=50
)
```

### Checking Order Status
```python
# Check status of a previous order
order_status = await get_order_status("your_request_id_here")
```

### Estimating Gas Costs
```python
# Estimate gas cost for Ethereum transaction
gas_estimate = await estimate_gas_cost(1, 21000)
```

## Supported Chains

- Ethereum Mainnet (1)
- Optimism (10)
- BNB Smart Chain (56)
- Polygon (137)
- Arbitrum One (42161)
- Base (8453)
- Avalanche C-Chain (43114)

## Configuration

The server can be configured via environment variables:

- `WHEELX_BASE_URL`: Base URL for WheelX API (default: https://wheelx.fi)
- `WHEELX_TIMEOUT`: Request timeout in seconds (default: 30)

## Development

### Testing
Run the test script to verify functionality:
```bash
python test_mcp_server.py
```

### Adding New Tools
Add new tools by decorating functions with `@mcp.tool()`:

```python
@mcp.tool()
async def my_new_tool(param1: str, param2: int) -> Dict[str, Any]:
    """Description of your tool."""
    # Implementation here
    return {"result": "success"}
```

### Adding New Resources
Add new resources by decorating functions with `@mcp.resource()`:

```python
@mcp.resource("wheelx://my_resource/{param}")
async def get_my_resource(param: str) -> str:
    """Description of your resource."""
    # Implementation here
    return json.dumps({"data": "your_data"})
```

## Dependencies

- `fastmcp`: FastMCP framework for MCP servers
- `requests`: HTTP client for API calls
- `pydantic`: Data validation and settings management

## License

MIT License