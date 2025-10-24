# WheelX SDK

SDK for interacting with the WheelX quote API and executing token swap/bridge transactions.

## Overview

This SDK provides:
- **Python SDK**: Complete implementation for getting quotes and executing transactions
- **Go SDK**: Complete implementation for getting quotes and executing transactions
- **Documentation**: Comprehensive API documentation for the `/v1/quote` endpoint

## Quick Start

### Python

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

# Execute transaction (requires web3.py and private key)
# from wheelx_sdk import TransactionExecutor
# executor = TransactionExecutor("https://mainnet.infura.io/v3/YOUR_PROJECT_ID")
# transaction = executor.build_transaction(quote.tx, quote_request.from_address)
# tx_hash = executor.sign_and_send_transaction(transaction, "YOUR_PRIVATE_KEY")
```

### Go

```go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/your-username/wheelx-sdk/wheelx"
)

func main() {
	// Initialize SDK
	sdk := wheelx.NewWheelXSDK("")

	// Create quote request
	req := wheelx.QuoteRequest{
		FromChain:   1,
		ToChain:     1,
		FromToken:   "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", // USDC
		ToToken:     "0xdAC17F958D2ee523a2206206994597C13D831ec7",   // USDT
		FromAddress: "0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
		ToAddress:   "0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
		Amount:      1000000, // 1 USDC (6 decimals)
		Slippage:    &[]int{50}[0],
	}

	// Get quote
	ctx := context.Background()
	quote, err := sdk.GetQuote(ctx, req)
	if err != nil {
		log.Fatalf("Failed to get quote: %v", err)
	}

	fmt.Printf("Quote received: %s tokens\n", quote.AmountOut)
	fmt.Printf("Request ID: %s\n", quote.RequestId)

	// Execute transaction (requires go-ethereum and private key)
	// executor, err := wheelx.NewTransactionExecutor("https://mainnet.infura.io/v3/YOUR_PROJECT_ID")
	// if err != nil {
	//     log.Fatalf("Failed to create executor: %v", err)
	// }
	//
	// fromAddress := common.HexToAddress(req.FromAddress)
	// tx, err := executor.BuildEIP1559Transaction(ctx, quote.Tx, fromAddress)
	// if err != nil {
	//     log.Fatalf("Failed to build transaction: %v", err)
	// }
	//
	// txHash, err := executor.SignAndSendTransaction(ctx, tx, "YOUR_PRIVATE_KEY")
	// if err != nil {
	//     log.Fatalf("Failed to send transaction: %v", err)
	// }
}
```

## Installation

### Python

```bash
pip install requests
# For transaction execution:
pip install web3
```

### Go

```bash
go get github.com/ethereum/go-ethereum
```

## Features

### Quote API
- Get token swap/bridge quotes with detailed pricing
- Support for cross-chain bridging
- Slippage tolerance configuration
- Permit2 support for gasless approvals

### Transaction Execution
- Complete transaction building and signing
- Support for both legacy and EIP-1559 transactions
- Automatic gas estimation
- Transaction confirmation monitoring

### Order Tracking
- Track order status using request ID
- Monitor transaction progress
- Get detailed order information

## API Documentation

See [QUOTE_ENDPOINT_DOCUMENTATION.md](./QUOTE_ENDPOINT_DOCUMENTATION.md) for complete API reference.

## Error Handling

Both SDKs provide comprehensive error handling:
- Network errors
- API errors (4xx, 5xx)
- Transaction execution errors
- Timeout handling

## Security

- Never commit private keys to version control
- Use environment variables for sensitive data
- Validate all transaction data before signing
- Use official RPC endpoints

## Examples

See the example code in each SDK file for complete usage examples.

## Support

For API issues, contact WheelX support.
For SDK issues, open an issue in this repository.