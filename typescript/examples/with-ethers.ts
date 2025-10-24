#!/usr/bin/env ts-node

/**
 * Example showing integration with ethers.js for transaction execution
 */

import { WheelXSDK, QuoteRequest } from '../src/sdk';
import { TransactionExecutor } from '../src/transaction';
import { ethers } from 'ethers';

async function main() {
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
    amount: 1000000,
    slippage: 50,
  };

  try {
    // Get quote
    const quote = await sdk.getQuote(quoteRequest);
    console.log(`Quote received: ${quote.amount_out} USDT`);

    // Setup ethers provider and signer
    // Note: In a real application, use environment variables for private keys
    const provider = new ethers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID');

    // Example with private key (commented out for safety)
    // const privateKey = process.env.PRIVATE_KEY || 'YOUR_PRIVATE_KEY';
    // const signer = new ethers.Wallet(privateKey, provider);

    // Example with browser wallet (MetaMask)
    // const provider = new ethers.BrowserProvider(window.ethereum);
    // const signer = await provider.getSigner();

    // For demonstration, we'll create a mock signer
    const mockSigner = {
      sendTransaction: async (tx: any) => {
        console.log('Mock transaction:', tx);
        return {
          hash: '0x' + '0'.repeat(64),
          wait: async () => ({
            blockNumber: 12345678,
            status: 1,
            transactionHash: '0x' + '0'.repeat(64),
          }),
        };
      },
    } as ethers.Signer;

    // Initialize transaction executor
    const executor = new TransactionExecutor(provider, mockSigner);

    // Build transaction
    const transaction = await executor.buildTransaction(
      quote.tx,
      quoteRequest.from_address
    );

    console.log('Transaction built successfully');
    console.log(`To: ${transaction.to}`);
    console.log(`Value: ${transaction.value}`);
    console.log(`Gas Limit: ${transaction.gasLimit}`);

    // In a real application, uncomment to send the transaction
    // const result = await executor.signAndSendTransaction(transaction);
    // console.log(`Transaction sent: ${result.hash}`);
    //
    // const receipt = await result.wait();
    // console.log(`Transaction confirmed in block: ${receipt.blockNumber}`);

  } catch (error) {
    console.error('Error:', error);
  }
}

main().catch(console.error);