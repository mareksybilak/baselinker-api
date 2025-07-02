# Examples Documentation

This document provides comprehensive examples for using the BaseLinker API Python client.

## Table of Contents

- [Basic Setup](#basic-setup)
- [Order Management Examples](#order-management-examples)
- [Product Management Examples](#product-management-examples)
- [Inventory Management Examples](#inventory-management-examples)
- [Shipping Examples](#shipping-examples)
- [Error Handling Examples](#error-handling-examples)
- [Advanced Usage](#advanced-usage)

## Basic Setup

### Simple Client Initialization

```python
from baselinker import BaseLinkerClient

# Initialize with token
client = BaseLinkerClient("your-api-token")

# Initialize with custom timeout
client = BaseLinkerClient("your-api-token", timeout=60)
```

### Using Environment Variables

```python
import os
from baselinker import BaseLinkerClient

# Set environment variable
os.environ['BASELINKER_TOKEN'] = "your-api-token"

# Initialize client
token = os.getenv('BASELINKER_TOKEN')
client = BaseLinkerClient(token)
```

## Order Management Examples

### Fetching Orders

```python
import time
from datetime import datetime, timedelta

# Get orders from last 7 days
week_ago = int((datetime.now() - timedelta(days=7)).timestamp())
orders = client.orders.get_orders(date_from=week_ago)

print(f"Found {len(orders.get('orders', []))} orders")

for order in orders.get('orders', []):
    print(f"Order ID: {order['order_id']}")
    print(f"Status: {order['order_status']}")
    print(f"Total: {order['price_brutto']} {order['currency']}")
    print(f"Customer: {order['delivery_fullname']}")
    print("-" * 40)
```

### Creating New Order

```python
import time

# Create new order
new_order_data = {
    "order_source_id": 1,  # Your order source ID
    "date_add": int(time.time()),
    "user_comments": "Customer order via API",
    "phone": "+48123456789",
    "email": "customer@example.com",
    "delivery_method": "Courier",
    "delivery_price": 15.99,
    "delivery_fullname": "Jan Kowalski",
    "delivery_company": "Test Company",
    "delivery_address": "Test Street 123",
    "delivery_city": "Warsaw",
    "delivery_postcode": "00-001",
    "delivery_country_code": "PL",
    "invoice_fullname": "Jan Kowalski",
    "invoice_nip": "1234567890",
    "products": [
        {
            "name": "Test Product",
            "sku": "TEST-001",
            "price_brutto": 29.99,
            "tax_rate": 23,
            "quantity": 2
        }
    ]
}

try:
    result = client.orders.add_order(**new_order_data)
    order_id = result.get('order_id')
    print(f"Order created successfully with ID: {order_id}")
except Exception as e:
    print(f"Failed to create order: {e}")
```

### Order Status Management

```python
# Get order sources first
sources = client.orders.get_order_sources()
print("Available order sources:")
for source in sources.get('sources', []):
    print(f"ID: {source['id']}, Name: {source['name']}")

# Update order status
order_id = 12345
new_status_id = 2  # Confirmed status

try:
    result = client.orders.set_order_status(order_id=order_id, status_id=new_status_id)
    if result.get('status') == 'SUCCESS':
        print(f"Order {order_id} status updated successfully")
except Exception as e:
    print(f"Failed to update order status: {e}")

# Add product to existing order
product_data = {
    "order_id": order_id,
    "product_id": "NEW-PRODUCT-001",
    "name": "Additional Product",
    "price_brutto": 19.99,
    "tax_rate": 23,
    "quantity": 1
}

try:
    result = client.orders.add_order_product(**product_data)
    print(f"Product added to order with ID: {result.get('order_product_id')}")
except Exception as e:
    print(f"Failed to add product to order: {e}")
```

## Product Management Examples

### Working with Inventories

```python
# Get all inventories
inventories = client.products.get_inventories()
print("Available inventories:")

for inventory in inventories.get('inventories', []):
    print(f"ID: {inventory['inventory_id']}")
    print(f"Name: {inventory['name']}")
    print(f"Description: {inventory.get('description', 'N/A')}")
    print("-" * 30)

# Select first inventory for examples
if inventories.get('inventories'):
    inventory_id = inventories['inventories'][0]['inventory_id']
    print(f"Using inventory ID: {inventory_id}")
else:
    print("No inventories found")
    exit()
```

### Product Catalog Operations

```python
# Search for products
products = client.products.get_inventory_products_list(
    inventory_id=inventory_id,
    filter_name="laptop",
    filter_limit=10,
    filter_sort="name"
)

print(f"Found {len(products.get('products', []))} products")

# Get detailed product data
if products.get('products'):
    product_ids = [p['product_id'] for p in products['products'][:5]]
    detailed_data = client.products.get_inventory_products_data(
        inventory_id=inventory_id,
        products=product_ids
    )
    
    for product in detailed_data.get('products', []):
        print(f"Product: {product['name']}")
        print(f"SKU: {product.get('sku', 'N/A')}")
        print(f"Price: {product.get('price_brutto', 0)} PLN")
        print(f"Stock: {product.get('stock', 0)}")
        print("-" * 30)
```

### Adding New Products

```python
# Add new product
new_product = {
    "inventory_id": inventory_id,
    "product_id": "API-PRODUCT-001",
    "ean": "1234567890123",
    "sku": "API-SKU-001",
    "tax_rate": 23,
    "weight": 0.5,
    "width": 10,
    "height": 5,
    "length": 15,
    "category_id": 1,
    "prices": {
        "1": {  # Price group ID
            "price_netto": 24.39,
            "price_brutto": 29.99,
            "price_wholesale_netto": 20.33,
            "price_wholesale_brutto": 25.00
        }
    },
    "stock": {
        "1": 100  # Warehouse ID: stock level
    },
    "text_fields": {
        "name": "API Test Product",
        "description": "Product added via API",
        "description_extra1": "Additional description",
        "description_extra2": "Technical specs",
        "description_extra3": "Warranty info",
        "description_extra4": "Usage instructions"
    },
    "images": [
        {
            "url": "https://example.com/product-image.jpg",
            "title": "Main product image",
            "sort": 1
        }
    ]
}

try:
    result = client.products.add_inventory_product(**new_product)
    print(f"Product added successfully: {result.get('product_id')}")
except Exception as e:
    print(f"Failed to add product: {e}")
```

### Stock Management

```python
# Update product stock
stock_updates = {
    "inventory_id": inventory_id,
    "products": [
        {
            "product_id": "API-PRODUCT-001",
            "variant_id": 0,
            "stock": 150
        },
        {
            "product_id": "EXISTING-PRODUCT-002",
            "variant_id": 0,
            "stock": 75
        }
    ]
}

try:
    result = client.products.update_inventory_products_stock(**stock_updates)
    print(f"Stock update status: {result.get('status')}")
    if result.get('warnings'):
        print("Warnings:")
        for warning in result['warnings']:
            print(f"  - {warning}")
except Exception as e:
    print(f"Failed to update stock: {e}")

# Update product prices
price_updates = {
    "inventory_id": inventory_id,
    "products": [
        {
            "product_id": "API-PRODUCT-001",
            "variant_id": 0,
            "price_netto": 28.46,
            "price_brutto": 34.99
        }
    ]
}

try:
    result = client.products.update_inventory_products_prices(**price_updates)
    print(f"Price update status: {result.get('status')}")
except Exception as e:
    print(f"Failed to update prices: {e}")
```

## Inventory Management Examples

### Category Management

```python
# Get categories
categories = client.products.get_inventory_categories(inventory_id=inventory_id)
print("Product categories:")

def print_categories(cats, level=0):
    for cat in cats:
        indent = "  " * level
        print(f"{indent}{cat['category_id']}: {cat['name']}")
        if 'children' in cat:
            print_categories(cat['children'], level + 1)

print_categories(categories.get('categories', []))

# Add new category
new_category = {
    "inventory_id": inventory_id,
    "name": "API Test Category",
    "parent_id": 0  # Root category
}

try:
    result = client.products.add_inventory_category(**new_category)
    category_id = result.get('category_id')
    print(f"Category created with ID: {category_id}")
    
    # Add subcategory
    subcategory = {
        "inventory_id": inventory_id,
        "name": "API Subcategory",
        "parent_id": category_id
    }
    
    sub_result = client.products.add_inventory_category(**subcategory)
    print(f"Subcategory created with ID: {sub_result.get('category_id')}")
    
except Exception as e:
    print(f"Failed to create category: {e}")
```

### Warehouse Management

```python
# Get warehouses
warehouses = client.inventory.get_inventory_warehouses(inventory_id=inventory_id)
print("Warehouses:")

for warehouse in warehouses.get('warehouses', []):
    print(f"ID: {warehouse['warehouse_id']}")
    print(f"Name: {warehouse['name']}")
    print(f"Description: {warehouse.get('description', 'N/A')}")
    print(f"Stock Edition: {warehouse.get('stock_edition', False)}")
    print("-" * 30)

# Add new warehouse
new_warehouse = {
    "inventory_id": inventory_id,
    "name": "API Test Warehouse",
    "description": "Warehouse created via API",
    "stock_edition": True,
    "disable_stock_level_below_zero": True
}

try:
    result = client.inventory.add_inventory_warehouse(**new_warehouse)
    warehouse_id = result.get('warehouse_id')
    print(f"Warehouse created with ID: {warehouse_id}")
except Exception as e:
    print(f"Failed to create warehouse: {e}")
```

## Shipping Examples

### Courier Integration

```python
# Get available couriers
couriers = client.courier.get_couriers_list()
print("Available couriers:")

for courier in couriers.get('couriers', []):
    print(f"Code: {courier['courier_code']}")
    print(f"Name: {courier['name']}")
    print(f"Services: {courier.get('services', [])}")
    print("-" * 30)

# Create package for order
order_id = 12345
courier_code = "DPD"  # Use available courier

package_data = {
    "order_id": order_id,
    "courier_code": courier_code,
    "fields": {
        "size": "M",
        "weight": 2.5,
        "width": 30,
        "height": 20,
        "length": 40,
        "declared_content": "Electronics",
        "insurance": True,
        "insurance_value": 299.99
    }
}

try:
    result = client.courier.create_package(**package_data)
    package_id = result.get('package_id')
    tracking_number = result.get('tracking_number')
    
    print(f"Package created:")
    print(f"  Package ID: {package_id}")
    print(f"  Tracking: {tracking_number}")
    
    # Get shipping label
    if package_id:
        label_result = client.courier.get_label(package_id=package_id)
        if label_result.get('label'):
            print("Shipping label generated successfully")
            # Save label to file
            import base64
            label_data = base64.b64decode(label_result['label'])
            with open(f"label_{package_id}.pdf", "wb") as f:
                f.write(label_data)
            print(f"Label saved as label_{package_id}.pdf")
            
except Exception as e:
    print(f"Failed to create package: {e}")
```

### Parcel Pickup

```python
# Request parcel pickup
pickup_data = {
    "courier_code": "DPD",
    "package_ids": [package_id] if 'package_id' in locals() else [123, 124],
    "pickup_date": "2024-01-15",
    "pickup_time_from": "10:00",
    "pickup_time_to": "16:00",
    "address": {
        "name": "Company Name",
        "street": "Business Street 123",
        "city": "Warsaw",
        "postcode": "00-001",
        "country": "PL",
        "phone": "+48123456789",
        "email": "pickup@company.com"
    }
}

try:
    result = client.courier.request_parcel_pickup(**pickup_data)
    print(f"Pickup requested:")
    print(f"  Pickup ID: {result.get('pickup_id')}")
    print(f"  Date: {result.get('pickup_date')}")
    print(f"  Time: {result.get('pickup_time')}")
except Exception as e:
    print(f"Failed to request pickup: {e}")
```

## Error Handling Examples

### Comprehensive Error Handling

```python
from baselinker import BaseLinkerClient
from baselinker.exceptions import (
    AuthenticationError,
    RateLimitError,
    APIError,
    BaseLinkerError
)
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_api_call(client, method_name, max_retries=3, **kwargs):
    """
    Safely call API method with error handling and retries
    """
    for attempt in range(max_retries):
        try:
            # For modular architecture, we need to access methods through modules
            # This is a simplified example - in practice you'd route to correct module
            if method_name.startswith('get_orders') or method_name in ['add_order', 'set_order_status']:
                method = getattr(client.orders, method_name.replace('get_orders', 'get_orders'))
            elif method_name in ['get_inventories']:
                method = getattr(client.products, method_name)
            else:
                # Generic fallback - determine correct module based on method name
                method = getattr(client.orders, method_name) if 'order' in method_name else getattr(client.products, method_name)
            result = method(**kwargs)
            logger.info(f"API call {method_name} successful")
            return result
            
        except AuthenticationError as e:
            logger.error(f"Authentication failed: {e}")
            raise  # Don't retry auth errors
            
        except RateLimitError as e:
            if attempt < max_retries - 1:
                wait_time = 60  # Wait 1 minute
                logger.warning(f"Rate limit hit, waiting {wait_time}s before retry {attempt + 1}")
                time.sleep(wait_time)
                continue
            else:
                logger.error(f"Rate limit exceeded after {max_retries} attempts")
                raise
                
        except APIError as e:
            logger.error(f"API error: {e} (code: {e.error_code})")
            if e.error_code in ['ERROR_TEMPORARY', 'ERROR_SERVER']:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    logger.info(f"Temporary error, retrying in {wait_time}s")
                    time.sleep(wait_time)
                    continue
            raise
            
        except BaseLinkerError as e:
            logger.error(f"Client error: {e}")
            raise
            
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise

# Usage example
client = BaseLinkerClient("your-token")

try:
    # Safe API calls with automatic retry
    orders = client.orders.get_orders(date_from=1640995200)
    inventories = client.products.get_inventories()
    
    print(f"Retrieved {len(orders.get('orders', []))} orders")
    print(f"Found {len(inventories.get('inventories', []))} inventories")
    
except Exception as e:
    print(f"API operation failed: {e}")
```

### Batch Operations with Error Handling

```python
def batch_update_stock(client, inventory_id, stock_updates, batch_size=50):
    """
    Update stock in batches with error handling
    """
    total_updates = len(stock_updates)
    successful_updates = 0
    failed_updates = []
    
    # Process in batches
    for i in range(0, total_updates, batch_size):
        batch = stock_updates[i:i + batch_size]
        
        try:
            result = client.products.update_inventory_products_stock(
                inventory_id=inventory_id,
                products=batch
            )
            
            successful_updates += len(batch)
            
            # Log warnings
            if result.get('warnings'):
                for warning in result['warnings']:
                    logger.warning(f"Stock update warning: {warning}")
                    
        except Exception as e:
            logger.error(f"Batch update failed for products {i}-{i+len(batch)}: {e}")
            failed_updates.extend([p['product_id'] for p in batch])
    
    print(f"Stock update complete:")
    print(f"  Successful: {successful_updates}/{total_updates}")
    print(f"  Failed: {len(failed_updates)}")
    
    if failed_updates:
        print(f"  Failed products: {failed_updates}")
    
    return successful_updates, failed_updates

# Example usage
stock_updates = [
    {"product_id": "PROD-001", "variant_id": 0, "stock": 100},
    {"product_id": "PROD-002", "variant_id": 0, "stock": 50},
    {"product_id": "PROD-003", "variant_id": 0, "stock": 200},
    # ... more products
]

successful, failed = batch_update_stock(client, inventory_id, stock_updates)
```

## Advanced Usage

### Custom Session Configuration

```python
import requests
from baselinker import BaseLinkerClient

# Create custom session with additional configuration
session = requests.Session()
session.headers.update({
    'User-Agent': 'MyApp/1.0',
    'Accept-Encoding': 'gzip, deflate'
})

# Configure retry strategy
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS", "POST"],
    backoff_factor=1
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

# Initialize client with custom session
client = BaseLinkerClient("your-token", timeout=45)
client.session = session
```

### Async-like Batch Processing

```python
import asyncio
import concurrent.futures
from functools import partial

def process_order_batch(client, order_ids):
    """Process a batch of orders"""
    results = []
    
    for order_id in order_ids:
        try:
            order_data = client.orders.get_orders(order_id=order_id)
            results.append(order_data)
        except Exception as e:
            logger.error(f"Failed to process order {order_id}: {e}")
            results.append(None)
    
    return results

def parallel_order_processing(client, all_order_ids, max_workers=5):
    """Process orders in parallel batches"""
    batch_size = 10
    batches = [all_order_ids[i:i + batch_size] 
              for i in range(0, len(all_order_ids), batch_size)]
    
    results = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all batches
        future_to_batch = {
            executor.submit(process_order_batch, client, batch): batch 
            for batch in batches
        }
        
        # Collect results
        for future in concurrent.futures.as_completed(future_to_batch):
            batch = future_to_batch[future]
            try:
                batch_results = future.result()
                results.extend(batch_results)
            except Exception as e:
                logger.error(f"Batch processing failed: {e}")
    
    return results

# Usage
order_ids = list(range(1000, 1100))  # Process orders 1000-1099
results = parallel_order_processing(client, order_ids)
valid_results = [r for r in results if r is not None]
print(f"Successfully processed {len(valid_results)} orders")
```

### Data Synchronization Example

```python
def sync_inventory_with_external_system(client, inventory_id, external_data):
    """
    Synchronize BaseLinker inventory with external system
    """
    # Get current inventory state
    current_products = client.products.get_inventory_products_list(
        inventory_id=inventory_id,
        filter_limit=1000
    )
    
    current_ids = {p['product_id'] for p in current_products.get('products', [])}
    external_ids = {p['id'] for p in external_data}
    
    # Find differences
    to_add = external_ids - current_ids
    to_update = external_ids & current_ids
    to_remove = current_ids - external_ids
    
    print(f"Sync plan:")
    print(f"  Add: {len(to_add)} products")
    print(f"  Update: {len(to_update)} products")
    print(f"  Remove: {len(to_remove)} products")
    
    # Add new products
    for external_product in external_data:
        if external_product['id'] in to_add:
            product_data = {
                "inventory_id": inventory_id,
                "product_id": external_product['id'],
                "text_fields": {
                    "name": external_product['name'],
                    "description": external_product.get('description', '')
                },
                "prices": {
                    "1": {
                        "price_brutto": external_product['price']
                    }
                },
                "stock": {
                    "1": external_product.get('stock', 0)
                }
            }
            
            try:
                client.products.add_inventory_product(**product_data)
                print(f"Added product: {external_product['id']}")
            except Exception as e:
                print(f"Failed to add {external_product['id']}: {e}")
    
    # Update existing products (stock and prices)
    stock_updates = []
    price_updates = []
    
    for external_product in external_data:
        if external_product['id'] in to_update:
            stock_updates.append({
                "product_id": external_product['id'],
                "variant_id": 0,
                "stock": external_product.get('stock', 0)
            })
            
            price_updates.append({
                "product_id": external_product['id'],
                "variant_id": 0,
                "price_brutto": external_product['price']
            })
    
    # Batch update stock and prices
    if stock_updates:
        try:
            client.products.update_inventory_products_stock(
                inventory_id=inventory_id,
                products=stock_updates
            )
            print(f"Updated stock for {len(stock_updates)} products")
        except Exception as e:
            print(f"Failed to update stock: {e}")
    
    if price_updates:
        try:
            client.products.update_inventory_products_prices(
                inventory_id=inventory_id,
                products=price_updates
            )
            print(f"Updated prices for {len(price_updates)} products")
        except Exception as e:
            print(f"Failed to update prices: {e}")
    
    # Remove obsolete products
    for product_id in to_remove:
        try:
            client.products.delete_inventory_product(
                inventory_id=inventory_id,
                product_id=product_id
            )
            print(f"Removed product: {product_id}")
        except Exception as e:
            print(f"Failed to remove {product_id}: {e}")

# Example external data
external_inventory = [
    {"id": "EXT-001", "name": "Product 1", "price": 29.99, "stock": 100},
    {"id": "EXT-002", "name": "Product 2", "price": 39.99, "stock": 50},
    {"id": "EXT-003", "name": "Product 3", "price": 19.99, "stock": 200},
]

sync_inventory_with_external_system(client, inventory_id, external_inventory)
```

This comprehensive examples documentation shows real-world usage patterns and best practices for the BaseLinker API Python client.