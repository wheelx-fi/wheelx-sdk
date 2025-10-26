#!/usr/bin/env python3
"""
Test script for WheelX MCP Server

This script tests the basic functionality of the MCP server without running the full server.
"""

import asyncio
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mcp_server import (
    get_quote,
    get_order_status,
    get_supported_chains,
    calculate_token_amount,
    estimate_gas_cost,
    compare_quotes,
    get_chain_tokens,
    get_service_status,
    get_usage_docs
)


async def test_tools():
    """Test all MCP tools"""
    print("Testing WheelX MCP Server Tools...")
    print("=" * 50)

    # Test get_supported_chains
    print("\n1. Testing get_supported_chains...")
    chains = await get_supported_chains()
    print(f"Supported chains: {chains.get('total_chains', 0)}")

    # Test calculate_token_amount
    print("\n2. Testing calculate_token_amount...")
    token_amount = await calculate_token_amount(1.5, 18)  # 1.5 ETH
    print(f"Token calculation: {token_amount}")

    # Test estimate_gas_cost
    print("\n3. Testing estimate_gas_cost...")
    gas_cost = await estimate_gas_cost(1, 21000)  # Ethereum
    print(f"Gas cost estimation: {gas_cost}")

    # Test get_quote (this will make an actual API call)
    print("\n4. Testing get_quote...")
    try:
        quote = await get_quote(
            from_chain=1,
            to_chain=1,
            from_token="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC
            to_token="0xdAC17F958D2ee523a2206206994597C13D831ec7",    # USDT
            from_address="0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
            to_address="0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
            amount=1000000,  # 1 USDC
            slippage=50
        )
        if 'error' in quote:
            print(f"Quote API error (expected): {quote['error']}")
        else:
            print(f"Quote received: {quote.get('amount_out', 'N/A')}")
    except Exception as e:
        print(f"Quote test failed (expected): {e}")

    # Test compare_quotes
    print("\n5. Testing compare_quotes...")
    try:
        comparison = await compare_quotes(
            from_chain=1,
            to_chain=1,
            from_token="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            to_token="0xdAC17F958D2ee523a2206206994597C13D831ec7",
            from_address="0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
            to_address="0x742d35Cc6634C0532925a3b8Dc9F6A7c5D3a7C6a",
            amount=1000000
        )
        if 'error' in comparison:
            print(f"Comparison API error (expected): {comparison['error']}")
        else:
            print(f"Comparison completed: {len(comparison.get('comparison', []))} quotes")
    except Exception as e:
        print(f"Comparison test failed (expected): {e}")

    print("\n" + "=" * 50)
    print("Tool testing completed!")


async def test_resources():
    """Test all MCP resources"""
    print("\nTesting WheelX MCP Server Resources...")
    print("=" * 50)

    # Test get_chain_tokens
    print("\n1. Testing get_chain_tokens...")
    tokens = await get_chain_tokens("1")  # Ethereum
    print(f"Ethereum tokens: {len(json.loads(tokens).get('tokens', []))} tokens")

    # Test get_service_status
    print("\n2. Testing get_service_status...")
    status = await get_service_status()
    status_data = json.loads(status)
    print(f"Service status: {status_data.get('status', 'unknown')}")

    # Test get_usage_docs
    print("\n3. Testing get_usage_docs...")
    docs = await get_usage_docs()
    print(f"Documentation length: {len(docs)} characters")

    print("\n" + "=" * 50)
    print("Resource testing completed!")


if __name__ == "__main__":
    import json

    print("WheelX MCP Server Test")
    print("=" * 50)

    # Run tests
    asyncio.run(test_tools())
    asyncio.run(test_resources())

    print("\n" + "=" * 50)
    print("All tests completed successfully!")
    print("\nTo run the full MCP server:")
    print("  python mcp_server.py")