#!/usr/bin/env python3
"""
Product management examples for BaseLinker API
"""

from baselinker import BaseLinkerClient
import os

def main():
    token = os.getenv('BASELINKER_TOKEN', 'your-api-token-here')
    client = BaseLinkerClient(token)
    
    try:
        # Get inventory products
        print("Getting inventory products...")
        products = client.products.get_inventory_products_list(
            inventory_id=123,  # Replace with your inventory ID
            filter_name="example"
        )
        print(f"Found {len(products.get('products', []))} products")
        
        # Add new product to inventory
        print("\nAdding new product...")
        new_product = {
            "inventory_id": 123,  # Replace with your inventory ID
            "product_id": "EXAMPLE_001",
            "name": "Example Product",
            "description": "This is an example product",
            "price_netto": 19.99,
            "price_brutto": 24.59,
            "tax_rate": 23,
            "weight": 0.5,
            "dimensions": "10x10x5"
        }
        
        result = client.products.add_inventory_product(**new_product)
        print(f"Product added with ID: {result.get('product_id')}")
        
        # Check product stock
        print("\nChecking product stock...")
        stock = client.products.get_inventory_products_stock(
            inventory_id=123,  # Replace with your inventory ID
            products=["EXAMPLE_001"]
        )
        print(f"Stock levels: {stock}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()