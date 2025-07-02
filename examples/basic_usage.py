#!/usr/bin/env python3
"""
Basic usage examples for BaseLinker API Python integration
"""

from baselinker import BaseLinkerClient
import os

def main():
    # Initialize client with API token
    token = os.getenv('BASELINKER_TOKEN', 'your-api-token-here')
    client = BaseLinkerClient(token)
    
    try:
        # Get list of inventories
        print("Getting inventories...")
        inventories = client.products.get_inventories()
        print(f"Found {len(inventories.get('inventories', []))} inventories")
        
        # Get orders from last 24 hours
        import time
        date_from = int(time.time()) - 86400  # 24 hours ago
        
        print(f"\nGetting orders from {date_from}...")
        orders = client.orders.get_orders(date_from=date_from)
        print(f"Found {len(orders.get('orders', []))} orders")
        
        # Get product categories (need inventory_id)
        if inventories.get('inventories'):
            inventory_id = inventories['inventories'][0]['inventory_id']
            print(f"\nGetting categories for inventory {inventory_id}...")
            categories = client.products.get_inventory_categories(inventory_id=inventory_id)
            print(f"Found {len(categories.get('categories', []))} categories")
        
        # Get couriers list
        print("\nGetting couriers...")
        couriers = client.courier.get_couriers_list()
        print(f"Found {len(couriers.get('couriers', []))} couriers")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()