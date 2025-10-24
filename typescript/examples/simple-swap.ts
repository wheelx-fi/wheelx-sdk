#!/usr/bin/env ts-node

/**
 * Simple token swap example using WheelX TypeScript SDK
 */

import { WheelXSDK, QuoteRequest } from '../src/sdk';

async function main() {
  // Initialize SDK
  const sdk = new WheelXSDK();

  // Create quote request for USDC to USDT swap on Ethereum
  const quoteRequest: QuoteRequest = {
    from_chain: 1, // Ethereum
    to_chain: 1, // Ethereum
    from_token: '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', // USDC
    to_token: '0xdAC17F958D2ee523a2206206994597C13D831ec7', // USDT
    from_address: '0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a',
    to_address: '0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a',
    amount: 1000000, // 1 USDC (6 decimals)
    slippage: 50, // 0.5% slippage
  };

  try {
    // Get quote
    const quote = await sdk.getQuote(quoteRequest);

    console.log('=== Quote Received ===');
    console.log(`Request ID: ${quote.request_id}`);
    console.log(`From: ${quoteRequest.amount} USDC`);
    console.log(`To: ${quote.amount_out} USDT`);
    console.log(`Fee: ${quote.fee} USDT`);
    console.log(`Min Receive: ${quote.min_receive} USDT`);
    console.log(`Slippage: ${quote.slippage / 100}%`);
    console.log(`Estimated Time: ${quote.estimated_time} seconds`);
    console.log(`Points Earned: ${quote.points}`);

    // Check if approval is needed
    if (quote.approve) {
      console.log('\n=== Approval Required ===');
      console.log(`Token: ${quote.approve.token}`);
      console.log(`Spender: ${quote.approve.spender}`);
      console.log(`Amount: ${quote.approve.amount}`);
    }

    // Show transaction details
    console.log('\n=== Transaction Details ===');
    console.log(`To: ${quote.tx.to}`);
    console.log(`Value: ${quote.tx.value} wei`);
    console.log(`Gas: ${quote.tx.gas}`);
    console.log(`Data: ${quote.tx.data.substring(0, 50)}...`);

    // Example of checking order status
    console.log('\n=== Order Status Query Example ===');
    console.log(`You can check order status later using request ID: ${quote.request_id}`);
    console.log('Example code:');
    console.log(`  const orderStatus = await sdk.getOrderStatus('${quote.request_id}');`);
    console.log(`  console.log('Order Status:', orderStatus.status);`);

    // Example of transaction execution (commented out for safety)
    // Uncomment and provide your private key to execute
    //
    // import { ethers } from 'ethers';
    // import { TransactionExecutor } from '../src/transaction';
    //
    // // Setup provider and signer
    // const provider = new ethers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID');
    // const privateKey = 'YOUR_PRIVATE_KEY';
    // const signer = new ethers.Wallet(privateKey, provider);
    //
    // const executor = new TransactionExecutor(provider, signer);
    // const result = await executor.executeQuoteTransaction(quote.tx, quoteRequest.from_address);
    //
    // console.log(`\nTransaction sent: ${result.hash}`);
    //
    // const receipt = await result.wait();
    // console.log(`Transaction confirmed in block: ${receipt?.blockNumber}`);

  } catch (error) {
    console.error('Error:', error);
  }
}

main().catch(console.error);