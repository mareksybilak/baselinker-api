#!/usr/bin/env python3
"""
BaseLinker API - Modular Usage Examples

This example shows how to use the new modular structure of the BaseLinker API client.
Each functionality is organized into specific modules for better code organization.
"""

import os
from baselinker import BaseLinkerClient

# Initialize client
API_TOKEN = os.getenv('BASELINKER_TOKEN', 'your_api_token_here')
client = BaseLinkerClient(API_TOKEN)

def demonstrate_orders_module():
    """Demonstrate orders module functionality"""
    print("=== Orders Module ===")
    
    # Get orders
    orders = client.orders.get_orders(filter_limit=10)
    print(f"Found {len(orders.get('orders', []))} orders")
    
    # Search orders by email
    email_orders = client.orders.get_orders_by_email(email="customer@example.com")
    print(f"Orders for email: {len(email_orders.get('orders', []))}")
    
    # Get order sources
    sources = client.orders.get_order_sources()
    print(f"Available order sources: {len(sources.get('sources', []))}")
    
    # Get order statuses
    statuses = client.orders.get_order_status_list()
    print(f"Available order statuses: {len(statuses.get('statuses', []))}")

def demonstrate_products_module():
    """Demonstrate products module functionality"""
    print("\n=== Products Module ===")
    
    # Get inventories
    inventories = client.products.get_inventories()
    print(f"Available inventories: {len(inventories.get('inventories', []))}")
    
    if inventories.get('inventories'):
        inventory_id = inventories['inventories'][0]['inventory_id']
        
        # Get products list
        products = client.products.get_inventory_products_list(
            inventory_id=inventory_id,
            filter_limit=5
        )
        print(f"Products in inventory {inventory_id}: {len(products.get('products', []))}")
        
        # Get categories
        categories = client.products.get_inventory_categories(inventory_id=inventory_id)
        print(f"Categories: {len(categories.get('categories', []))}")
        
        # Get manufacturers
        manufacturers = client.products.get_inventory_manufacturers(inventory_id=inventory_id)
        print(f"Manufacturers: {len(manufacturers.get('manufacturers', []))}")

def demonstrate_inventory_module():
    """Demonstrate inventory module functionality"""
    print("\n=== Inventory Module ===")
    
    inventories = client.products.get_inventories()
    if inventories.get('inventories'):
        inventory_id = inventories['inventories'][0]['inventory_id']
        
        # Get warehouses
        warehouses = client.inventory.get_inventory_warehouses(inventory_id=inventory_id)
        print(f"Warehouses: {len(warehouses.get('warehouses', []))}")
        
        # Get price groups
        price_groups = client.inventory.get_inventory_price_groups(inventory_id=inventory_id)
        print(f"Price groups: {len(price_groups.get('price_groups', []))}")

def demonstrate_courier_module():
    """Demonstrate courier module functionality"""
    print("\n=== Courier Module ===")
    
    # Get couriers list
    couriers = client.courier.get_couriers_list()
    print(f"Available couriers: {len(couriers.get('couriers', []))}")
    
    if couriers.get('couriers'):
        courier_code = couriers['couriers'][0]['courier_code']
        
        # Get courier services
        services = client.courier.get_courier_services(courier_code=courier_code)
        print(f"Services for {courier_code}: {len(services.get('services', []))}")

def demonstrate_invoices_module():
    """Demonstrate invoices module functionality"""
    print("\n=== Invoices Module ===")
    
    # Get invoices
    invoices = client.invoices.get_invoices()
    print(f"Recent invoices: {len(invoices.get('invoices', []))}")
    
    # Get document series
    series = client.invoices.get_series()
    print(f"Document series: {len(series.get('series', []))}")

def demonstrate_returns_module():
    """Demonstrate returns module functionality"""
    print("\n=== Returns Module ===")
    
    # Get order returns
    returns = client.returns.get_order_returns()
    print(f"Recent returns: {len(returns.get('returns', []))}")
    
    # Get return statuses
    statuses = client.returns.get_order_return_status_list()
    print(f"Return statuses: {len(statuses.get('statuses', []))}")
    
    # Get return reasons
    reasons = client.returns.get_order_return_reasons_list()
    print(f"Return reasons: {len(reasons.get('reasons', []))}")

def demonstrate_external_storage_module():
    """Demonstrate external storage module functionality"""
    print("\n=== External Storage Module ===")
    
    # Get external storages
    storages = client.external_storage.get_external_storages_list()
    print(f"Connected external storages: {len(storages.get('storages', []))}")

def demonstrate_documents_module():
    """Demonstrate documents module functionality"""
    print("\n=== Documents Module ===")
    
    inventories = client.products.get_inventories()
    if inventories.get('inventories'):
        inventory_id = inventories['inventories'][0]['inventory_id']
        
        # Get warehouse documents
        documents = client.documents.get_inventory_documents(inventory_id=inventory_id)
        print(f"Warehouse documents: {len(documents.get('documents', []))}")
        
        # Get purchase orders
        purchase_orders = client.documents.get_inventory_purchase_orders(inventory_id=inventory_id)
        print(f"Purchase orders: {len(purchase_orders.get('purchase_orders', []))}")

def demonstrate_devices_module():
    """Demonstrate devices module functionality"""
    print("\n=== Devices Module ===")
    
    # Get printers
    printers = client.devices.get_printers()
    print(f"Registered printers: {len(printers.get('printers', []))}")
    
    # Get Connect integrations
    integrations = client.devices.get_connect_integrations()
    print(f"Connect integrations: {len(integrations.get('integrations', []))}")

def main():
    """Main demonstration function"""
    print("BaseLinker API - Modular Structure Demonstration")
    print("=" * 50)
    
    try:
        # Modular approach
        print("=== Modular API Usage ===")
        demonstrate_orders_module()
        demonstrate_products_module()
        demonstrate_inventory_module()
        demonstrate_courier_module()
        demonstrate_invoices_module()
        demonstrate_returns_module()
        demonstrate_external_storage_module()
        demonstrate_documents_module()
        demonstrate_devices_module()
        
        print("\n" + "=" * 50)
        print("✓ All modules demonstrated successfully!")
        print("\nKey Benefits of Modular Structure:")
        print("• Better code organization")
        print("• Clear separation of concerns")
        print("• Easier to find relevant methods")
        print("• Extended functionality with 50+ new methods")
        print("• Type safety and parameter validation")
        
    except Exception as e:
        print(f"❌ Error during demonstration: {e}")
        print("Make sure you have a valid API token set in BASELINKER_TOKEN environment variable")

if __name__ == "__main__":
    main()