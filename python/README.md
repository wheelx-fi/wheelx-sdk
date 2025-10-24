# WheelX Python SDK

Python SDK for interacting with the WheelX quote API and executing token swap/bridge transactions.

## Installation

### Basic Installation

```bash
pip install wheelx-sdk
```

### With Web3 Support (for transaction execution)

```bash
pip install wheelx-sdk[web3]
```

### From Source

```bash
git clone https://github.com/wheelx/wheelx-sdk-python.git
cd wheelx-sdk-python
pip install -e .
```

## Quick Start

```python
from wheelx_sdk import WheelXSDK, QuoteRequest

# Initialize SDK
sdk = WheelXSDK()

# Create quote request
quote_request = QuoteRequest(
    from_chain=1,
    to_chain=1,
    from_token="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC
    to_token="0xdAC17F958D2ee523a2206206994597C13D831ec7",    # USDT
    from_address="0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
    to_address="0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
    amount=1000000,  # 1 USDC (6 decimals)
    slippage=50
)

# Get quote
quote = sdk.get_quote(quote_request)
print(f"Quote received: {quote.amount_out} tokens")
print(f"Request ID: {quote.request_id}")
print(f"Min receive: {quote.min_receive}")

# Check if approval is needed
if quote.approve:
    print(f"Approval needed for token: {quote.approve.token}")
    print(f"Spender: {quote.approve.spender}")
    print(f"Amount: {quote.approve.amount}")
```

## Transaction Execution

```python
from wheelx_sdk import TransactionExecutor

# Initialize transaction executor
executor = TransactionExecutor("https://mainnet.infura.io/v3/YOUR_PROJECT_ID")

# Build transaction
transaction = executor.build_transaction(quote.tx, quote_request.from_address)

# Sign and send transaction (requires private key)
tx_hash = executor.sign_and_send_transaction(transaction, "YOUR_PRIVATE_KEY")
print(f"Transaction sent: {tx_hash}")

# Wait for confirmation
receipt = executor.wait_for_transaction(tx_hash)
print(f"Transaction confirmed in block: {receipt.blockNumber}")
```

## API Reference

### WheelXSDK

- `get_quote(quote_request: QuoteRequest) -> QuoteResponse`: Get a quote for token swap/bridge
- `get_order_status(request_id: str) -> Dict[str, Any]`: Get order status by request ID

### TransactionExecutor

- `build_transaction(tx_data: Tx, account_address: str) -> Dict[str, Any]`: Build transaction dictionary for signing
- `sign_and_send_transaction(transaction: Dict[str, Any], private_key: str) -> str`: Sign and send transaction
- `wait_for_transaction(tx_hash: str, timeout: int = 300) -> Dict[str, Any]`: Wait for transaction confirmation

## Data Models

### QuoteRequest

```python
QuoteRequest(
    from_chain: int,
    to_chain: int,
    from_token: str,
    to_token: str,
    from_address: str,
    to_address: str,
    amount: int,
    slippage: Optional[int] = None,
)
```

### QuoteResponse

```python
QuoteResponse(
    request_id: str,
    amount_out: str,
    fee: str,
    tx: Tx,
    approve: Optional[ApproveAction],
    slippage: int,
    min_receive: str,
    estimated_time: int,
    recipient: str,
    router_type: str,
    price_impact: PriceImpactFormatted,
    router: str,
    created_at: str,
    points: str
)
```

## Error Handling

```python
try:
    quote = sdk.get_quote(quote_request)
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

## Examples

See the `examples/` directory for complete usage examples:

- `simple_swap.py`: Basic token swap
- `cross_chain_bridge.py`: Cross-chain bridging
- `with_approval.py`: Swap with token approval

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/wheelx/wheelx-sdk-python.git
cd wheelx-sdk-python

# Install in development mode
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
pytest
```

### Building Package

```bash
python setup.py sdist bdist_wheel
```

## License

MIT License
