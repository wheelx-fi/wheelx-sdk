#!/usr/bin/env python3
"""
Simple token swap example using WheelX SDK
"""

import os
from wheelx_sdk import WheelXSDK, QuoteRequest


def main():
    # Initialize SDK
    sdk = WheelXSDK()

    # Create quote request for USDC to USDT swap on Ethereum
    quote_request = QuoteRequest(
        from_chain=1,  # Ethereum
        to_chain=1,    # Ethereum
        from_token="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC
        to_token="0xdAC17F958D2ee523a2206206994597C13D831ec7",    # USDT
        from_address="0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
        to_address="0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
        amount=1000000,  # 1 USDC (6 decimals)
        slippage=50      # 0.5% slippage
    )

    try:
        # Get quote
        quote = sdk.get_quote(quote_request)

        print("=== Quote Received ===")
        print(f"Request ID: {quote.request_id}")
        print(f"From: {quote_request.amount} USDC")
        print(f"To: {quote.amount_out} USDT")
        print(f"Fee: {quote.fee} USDT")
        print(f"Min Receive: {quote.min_receive} USDT")
        print(f"Slippage: {quote.slippage / 100}%")
        print(f"Estimated Time: {quote.estimated_time} seconds")
        print(f"Points Earned: {quote.points}")

        # Check if approval is needed
        if quote.approve:
            print(f"\n=== Approval Required ===")
            print(f"Token: {quote.approve.token}")
            print(f"Spender: {quote.approve.spender}")
            print(f"Amount: {quote.approve.amount}")

        # Show transaction details
        print(f"\n=== Transaction Details ===")
        print(f"To: {quote.tx.to}")
        print(f"Value: {quote.tx.value} wei")
        print(f"Gas: {quote.tx.gas}")
        print(f"Data: {quote.tx.data[:50]}...")

        # Example of checking order status
        print(f"\n=== Order Status Query Example ===")
        print(f"You can check order status later using request ID: {quote.request_id}")
        print("Example code:")
        print(f"  order_status = sdk.get_order_status('{quote.request_id}')")
        print(f"  print('Order Status:', order_status.status)")

        # Example of transaction execution (commented out for safety)
        # Uncomment and provide your private key to execute
        #
        # from wheelx_sdk import TransactionExecutor
        # executor = TransactionExecutor("https://mainnet.infura.io/v3/YOUR_PROJECT_ID")
        # transaction = executor.build_transaction(quote.tx, quote_request.from_address)
        # tx_hash = executor.sign_and_send_transaction(transaction, "YOUR_PRIVATE_KEY")
        # print(f"\nTransaction sent: {tx_hash}")
        # receipt = executor.wait_for_transaction(tx_hash)
        # print(f"Transaction confirmed in block: {receipt.blockNumber}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()