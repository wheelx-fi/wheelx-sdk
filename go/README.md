# WheelX Go SDK

Go SDK for interacting with the WheelX quote API and executing token swap/bridge transactions.

## Installation

```bash
go get github.com/wheelx/wheelx-sdk-go
```

## Quick Start

```go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/wheelx/wheelx-sdk-go/wheelx"
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
	fmt.Printf("Min receive: %s\n", quote.MinReceive)

	// Check if approval is needed
	if quote.Approve != nil {
		fmt.Printf("Approval needed for token: %s\n", quote.Approve.Token)
		fmt.Printf("Spender: %s\n", quote.Approve.Spender)
		fmt.Printf("Amount: %d\n", quote.Approve.Amount)
	}
}
```

## Transaction Execution

```go
import (
	"context"
	"fmt"
	"log"

	"github.com/ethereum/go-ethereum/common"
	"github.com/wheelx/wheelx-sdk-go/wheelx"
)

func main() {
	// Initialize SDK and executor
	sdk := wheelx.NewWheelXSDK("")
	executor, err := wheelx.NewTransactionExecutor("https://mainnet.infura.io/v3/YOUR_PROJECT_ID")
	if err != nil {
		log.Fatalf("Failed to create executor: %v", err)
	}

	// Get quote (previous example)
	// ...

	// Build and send transaction
	ctx := context.Background()
	fromAddress := common.HexToAddress(req.FromAddress)
	tx, err := executor.BuildEIP1559Transaction(ctx, quote.Tx, fromAddress)
	if err != nil {
		log.Fatalf("Failed to build transaction: %v", err)
	}

	txHash, err := executor.SignAndSendTransaction(ctx, tx, "YOUR_PRIVATE_KEY")
	if err != nil {
		log.Fatalf("Failed to send transaction: %v", err)
	}

	fmt.Printf("Transaction sent: %s\n", txHash.Hex())

	// Wait for confirmation
	receipt, err := executor.WaitForTransaction(ctx, txHash)
	if err != nil {
		log.Fatalf("Failed to wait for transaction: %v", err)
	}

	fmt.Printf("Transaction confirmed in block: %d\n", receipt.BlockNumber)
}
```

## API Reference

### WheelXSDK

- `NewWheelXSDK(baseURL string) *WheelXSDK`: Create new SDK instance
- `GetQuote(ctx context.Context, req QuoteRequest) (*QuoteResponse, error)`: Get quote for token swap/bridge
- `GetOrderStatus(ctx context.Context, requestID string) (*OrderResponse, error)`: Get order status by request ID

### TransactionExecutor

- `NewTransactionExecutor(rpcURL string) (*TransactionExecutor, error)`: Create new transaction executor
- `BuildTransaction(ctx context.Context, txData Tx, fromAddress common.Address) (*types.Transaction, error)`: Build legacy transaction
- `BuildEIP1559Transaction(ctx context.Context, txData Tx, fromAddress common.Address) (*types.Transaction, error)`: Build EIP-1559 transaction
- `SignAndSendTransaction(ctx context.Context, tx *types.Transaction, privateKey string) (common.Hash, error)`: Sign and send transaction
- `WaitForTransaction(ctx context.Context, txHash common.Hash) (*types.Receipt, error)`: Wait for transaction confirmation

## Data Models

### QuoteRequest

```go
type QuoteRequest struct {
	FromChain   int    `json:"from_chain"`
	ToChain     int    `json:"to_chain"`
	FromToken   string `json:"from_token"`
	ToToken     string `json:"to_token"`
	FromAddress string `json:"from_address"`
	ToAddress   string `json:"to_address"`
	Amount      int    `json:"amount"`
	Slippage    *int   `json:"slippage,omitempty"`
}
```

### QuoteResponse

```go
type QuoteResponse struct {
	RequestId     string              `json:"request_id"`
	AmountOut     string              `json:"amount_out"`
	Fee           string              `json:"fee"`
	Tx            Tx                  `json:"tx"`
	Approve       *ApproveAction      `json:"approve,omitempty"`
	Slippage      int                 `json:"slippage"`
	MinReceive    string              `json:"min_receive"`
	EstimatedTime int                 `json:"estimated_time"`
	Recipient     string              `json:"recipient"`
	RouterType    string              `json:"router_type"`
	PriceImpact   PriceImpactFormatted `json:"price_impact"`
	Router        string              `json:"router"`
	CreatedAt     string              `json:"created_at"`
	Points        string              `json:"points"`
}
```

## Error Handling

```go
quote, err := sdk.GetQuote(ctx, req)
if err != nil {
	// Handle different error types
	if strings.Contains(err.Error(), "API request failed") {
		// API error
		log.Printf("API error: %v", err)
	} else if strings.Contains(err.Error(), "failed to send request") {
		// Network error
		log.Printf("Network error: %v", err)
	} else {
		// Other errors
		log.Printf("Unexpected error: %v", err)
	}
	return
}
```

## Examples

See the `examples/` directory for complete usage examples:

- `simple_swap.go`: Basic token swap
- `cross_chain_bridge.go`: Cross-chain bridging
- `with_approval.go`: Swap with token approval

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/wheelx/wheelx-sdk-go.git
cd wheelx-sdk-go

# Download dependencies
go mod download

# Run tests
go test ./...

# Build package
go build ./pkg/wheelx
```

### Running Tests

```bash
go test -v ./...
```

## License

MIT License
