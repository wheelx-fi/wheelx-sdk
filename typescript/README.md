# WheelX TypeScript SDK

TypeScript SDK for interacting with the WheelX quote API and executing token swap/bridge transactions.

## Installation

### Using npm

```bash
npm install @wheelx/sdk ethers
```

### Using yarn

```bash
yarn add @wheelx/sdk ethers
```

### Using pnpm

```bash
pnpm add @wheelx/sdk ethers
```

## Quick Start

```typescript
import { WheelXSDK, QuoteRequest } from '@wheelx/sdk';

// Initialize SDK
const sdk = new WheelXSDK();

// Create quote request
const quoteRequest: QuoteRequest = {
  from_chain: 1,
  to_chain: 1,
  from_token: '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', // USDC
  to_token: '0xdAC17F958D2ee523a2206206994597C13D831ec7', // USDT
  from_address: '0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a',
  to_address: '0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a',
  amount: 1000000, // 1 USDC (6 decimals)
  slippage: 50, // 0.5% slippage
};

// Get quote
try {
  const quote = await sdk.getQuote(quoteRequest);

  console.log(`Quote received: ${quote.amount_out} tokens`);
  console.log(`Request ID: ${quote.request_id}`);
  console.log(`Min receive: ${quote.min_receive}`);

  // Check if approval is needed
  if (quote.approve) {
    console.log(`Approval needed for token: ${quote.approve.token}`);
    console.log(`Spender: ${quote.approve.spender}`);
    console.log(`Amount: ${quote.approve.amount}`);
  }
} catch (error) {
  console.error('Error getting quote:', error);
}
```

## Transaction Execution

```typescript
import { WheelXSDK, TransactionExecutor } from '@wheelx/sdk';
import { ethers } from 'ethers';

// Initialize SDK and executor
const sdk = new WheelXSDK();

// Setup ethers provider and signer
const provider = new ethers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID');
const privateKey = 'YOUR_PRIVATE_KEY'; // Use environment variables in production
const signer = new ethers.Wallet(privateKey, provider);

const executor = new TransactionExecutor(provider, signer);

// Get quote (from previous example)
const quote = await sdk.getQuote(quoteRequest);

// Execute transaction
try {
  const result = await executor.executeQuoteTransaction(
    quote.tx,
    quoteRequest.from_address
  );

  console.log(`Transaction sent: ${result.hash}`);

  // Wait for confirmation
  const receipt = await result.wait();
  console.log(`Transaction confirmed in block: ${receipt.blockNumber}`);
} catch (error) {
  console.error('Error executing transaction:', error);
}
```

## Browser Usage (MetaMask)

```typescript
import { WheelXSDK, TransactionExecutor } from '@wheelx/sdk';
import { ethers } from 'ethers';

// Check if MetaMask is available
if (typeof window.ethereum !== 'undefined') {
  // Initialize browser provider
  const provider = new ethers.BrowserProvider(window.ethereum);

  // Request account access
  await window.ethereum.request({ method: 'eth_requestAccounts' });

  // Get signer
  const signer = await provider.getSigner();

  // Initialize SDK and executor
  const sdk = new WheelXSDK();
  const executor = new TransactionExecutor(provider, signer);

  // Get user address
  const fromAddress = await signer.getAddress();

  // Create quote request with user's address
  const quoteRequest: QuoteRequest = {
    from_chain: 1,
    to_chain: 1,
    from_token: '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
    to_token: '0xdAC17F958D2ee523a2206206994597C13D831ec7',
    from_address: fromAddress,
    to_address: fromAddress,
    amount: 1000000,
    slippage: 50,
  };

  // Get quote and execute transaction
  const quote = await sdk.getQuote(quoteRequest);
  const result = await executor.executeQuoteTransaction(quote.tx, fromAddress);

  console.log(`Transaction sent: ${result.hash}`);
}
```

## API Reference

### WheelXSDK

- `constructor(config?: SDKConfig)`: Create new SDK instance
- `getQuote(quoteRequest: QuoteRequest): Promise<QuoteResponse>`: Get quote for token swap/bridge
- `getOrderStatus(requestId: string): Promise<OrderResponse>`: Get order status by request ID

### TransactionExecutor

- `constructor(provider: ethers.Provider | string, signer?: ethers.Signer)`: Create new executor
- `setSigner(signer: ethers.Signer): void`: Set signer for transaction execution
- `buildTransaction(txData: Tx, fromAddress: string, config?: TransactionConfig): Promise<ethers.TransactionRequest>`: Build transaction
- `signAndSendTransaction(transaction: ethers.TransactionRequest): Promise<TransactionResult>`: Sign and send transaction
- `executeQuoteTransaction(txData: Tx, fromAddress: string, config?: TransactionConfig): Promise<TransactionResult>`: Execute quote transaction
- `waitForTransaction(txHash: string, confirmations?: number, timeout?: number): Promise<ethers.TransactionReceipt>`: Wait for transaction confirmation

## Data Models

### QuoteRequest

```typescript
interface QuoteRequest {
  from_chain: number;
  to_chain: number;
  from_token: string;
  to_token: string;
  from_address: string;
  to_address: string;
  amount: number;
  slippage?: number;
}
```

### QuoteResponse

```typescript
interface QuoteResponse {
  request_id: string;
  amount_out: string;
  fee: string;
  tx: Tx;
  approve?: ApproveAction;
  slippage: number;
  min_receive: string;
  estimated_time: number;
  recipient: string;
  router_type: string;
  price_impact: PriceImpactFormatted;
  router: string;
  created_at: string;
  points: string;
}
```

## Error Handling

```typescript
import { APIError, NetworkError, ValidationError } from '@wheelx/sdk';

try {
  const quote = await sdk.getQuote(quoteRequest);
} catch (error) {
  if (error instanceof APIError) {
    console.error('API Error:', error.message, error.statusCode);
  } else if (error instanceof NetworkError) {
    console.error('Network Error:', error.message);
  } else if (error instanceof ValidationError) {
    console.error('Validation Error:', error.message);
  } else {
    console.error('Unexpected Error:', error);
  }
}
```

## Examples

See the `examples/` directory for complete usage examples:

- `simple-swap.ts`: Basic token swap
- `with-ethers.ts`: Integration with ethers.js

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/wheelx/wheelx-sdk-typescript.git
cd wheelx-sdk-typescript

# Install dependencies
npm install

# Build package
npm run build

# Run tests
npm test

# Run linting
npm run lint
```

### Running Examples

```bash
# Run simple swap example
npx ts-node examples/simple-swap.ts

# Run ethers integration example
npx ts-node examples/with-ethers.ts
```

### Building for Production

```bash
npm run build
```

## Browser Support

This SDK works in both Node.js and browser environments. For browser usage:

1. Include the SDK in your bundle
2. Ensure `ethers` is available
3. Use a browser provider (like MetaMask)

## License

MIT License
