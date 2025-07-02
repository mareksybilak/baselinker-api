# BaseLinker API Methods Documentation

Complete documentation for all BaseLinker API methods in the modular Python client. This library provides **133 methods** across **9 specialized modules** with **82% test coverage**.

**Python Client Features:**
- 🏗️ **Modular Architecture** - Organized by functional areas
- 📈 **Comprehensive Coverage** - 133 API methods across 9 modules
- 🔒 **Type Safety** - Parameter validation and error handling
- 🧪 **Well Tested** - 82% test coverage with 300+ test methods
- 🚀 **Easy to Use** - Intuitive module-based interface

Based on official API documentation at https://api.baselinker.com

## Table of Contents

- [API Overview](#api-overview)
- [Modular Architecture](#modular-architecture)
- [Order Management Methods](#order-management-methods)
- [Product Catalog Methods](#product-catalog-methods)
- [Inventory Management Methods](#inventory-management-methods)
- [Courier & Shipping Methods](#courier--shipping-methods)
- [Invoice & Payment Methods](#invoice--payment-methods)
- [Returns Management Methods](#returns-management-methods)
- [External Storage Methods](#external-storage-methods)
- [Document Management Methods](#document-management-methods)
- [Device Management Methods](#device-management-methods)
- [Response Formats](#response-formats)
- [Error Handling](#error-handling)

## API Overview

- **Base URL**: `https://api.baselinker.com/connector.php`
- **Rate Limit**: 100 requests per minute
- **Encoding**: UTF-8
- **Authentication**: API token via `X-BLToken` header
- **Data Format**: JSON

## Modular Architecture

The BaseLinker Python client is organized into specialized modules for better code organization and ease of use:

```python
from baselinker import BaseLinkerClient

# Initialize client with API token
client = BaseLinkerClient("your-api-token")

# 🛒 Orders Management (24 methods)
client.orders.get_orders(date_from=1640995200)
client.orders.add_order(order_source_id=1, date_add=1640995200, order_status_id=1)
client.orders.get_orders_by_email(email="customer@example.com")
client.orders.set_order_status(order_id=123, status_id=2)

# 📦 Product Catalog (30 methods)  
client.products.get_inventories()
client.products.get_inventory_products_list(inventory_id=123)
client.products.add_inventory_product(inventory_id=123, product_id="PROD-001")
client.products.update_inventory_products_stock(inventory_id=123, products=[])

# 🏪 Inventory Management (8 methods)
client.inventory.get_inventory_warehouses(inventory_id=123)
client.inventory.add_inventory_warehouse(inventory_id=123, name="New Warehouse")
client.inventory.get_inventory_price_groups(inventory_id=123)

# 🚚 Courier Services (14 methods)
client.courier.get_couriers_list()
client.courier.create_package(order_id=123, courier_code="dpd")
client.courier.get_label(package_id=456)
client.courier.request_parcel_pickup(courier_code="dpd", package_ids=[123])

# 💰 Invoices & Payments (10 methods)
client.invoices.add_invoice(order_id=123)
client.invoices.get_invoices()
client.invoices.set_order_payment(order_id=123, payment_done=1)

# 🔄 Returns Management (11 methods)
client.returns.add_order_return(order_id=123)
client.returns.get_order_returns()
client.returns.set_order_return_status(return_id=123, status_id=1)

# 🌐 External Storage (8 methods)
client.external_storage.get_external_storages_list()
client.external_storage.get_external_storage_products_data(storage_id="123", products=["PROD-001"])

# 📋 Document Management (8 methods)
client.documents.get_inventory_documents(inventory_id=123)
client.documents.get_inventory_purchase_orders(inventory_id=123)

# 🔧 Device Management (20 methods)
client.devices.get_printers()
client.devices.get_connect_integrations()
client.devices.add_log(log_type="info", message="Log message")
```

### Module Summary

| Module | Methods | Description |
|--------|---------|-------------|
| **orders** | 24 | Order lifecycle management, search, and transactions |
| **products** | 30 | Product catalog, inventory, categories, and manufacturers |
| **inventory** | 8 | Warehouse and price group management |
| **courier** | 14 | Shipping, package creation, and courier integration |
| **invoices** | 10 | Invoice generation and payment processing |
| **returns** | 11 | Return management and processing |
| **external_storage** | 8 | External marketplace integration |
| **documents** | 8 | Document and purchase order management |
| **devices** | 20 | Printer, scale, and automation device management |
| **Total** | **133** | **Complete BaseLinker API coverage** |

## Order Management Methods

### get_orders(**kwargs)

Download orders from BaseLinker order manager.

**Parameters:**
- `order_id` (int, optional): Specific order identifier
- `date_confirmed_from` (int, optional): Unix timestamp - confirmed orders from this date
- `date_from` (int, optional): Unix timestamp - orders created from this date  
- `date_to` (int, optional): Unix timestamp - orders created until this date
- `id_from` (int, optional): Order ID to start collecting subsequent orders
- `id_to` (int, optional): Order ID to end collecting orders
- `get_unconfirmed_orders` (bool, optional): Include unconfirmed orders (default: false)
- `include_custom_extra_fields` (bool, optional): Download custom field values (default: false)
- `status_id` (int, optional): Filter by specific order status
- `filter_email` (varchar(50), optional): Filter by customer email
- `filter_order_source` (varchar(20), optional): Filter by order source
- `filter_order_source_id` (int, optional): Specific order source identifier
- `with_commission` (bool, optional): Include commission information (default: false)

**Limitations:** Maximum 100 orders per request

**Returns:** 
```json
{
    "status": "SUCCESS",
    "orders": [
        {
            "order_id": 123,
            "shop_order_id": "SHOP-456",
            "external_order_id": "EXT-789",
            "order_source": "shop",
            "order_source_id": 1,
            "order_source_info": "My Shop",
            "order_status_id": 2,
            "date_add": 1640995200,
            "date_confirmed": 1640995800,
            "date_in_status": 1640996400,
            "user_login": "customer@email.com",
            "phone": "+48123456789",
            "email": "customer@email.com",
            "user_comments": "Please deliver after 6 PM",
            "admin_comments": "VIP customer",
            "currency": "PLN",
            "payment_method": "Credit Card",
            "payment_method_cod": false,
            "payment_done": 1,
            "delivery_method": "DPD Courier",
            "delivery_price": 15.99,
            "delivery_fullname": "John Doe",
            "delivery_company": "ACME Corp",
            "delivery_address": "Main Street 123",
            "delivery_city": "Warsaw",
            "delivery_postcode": "00-001",
            "delivery_country_code": "PL",
            "delivery_point_id": "",
            "delivery_point_name": "",
            "delivery_point_address": "",
            "delivery_point_postcode": "",
            "delivery_point_city": "",
            "invoice_fullname": "John Doe",
            "invoice_company": "ACME Corp",
            "invoice_nip": "1234567890",
            "invoice_address": "Main Street 123",
            "invoice_city": "Warsaw",
            "invoice_postcode": "00-001",
            "invoice_country_code": "PL",
            "want_invoice": true,
            "extra_field_1": "",
            "extra_field_2": "",
            "order_page": "",
            "pick_state": 0,
            "pack_state": 0,
            "products": [
                {
                    "order_product_id": 456,
                    "storage": "bl",
                    "storage_id": 0,
                    "product_id": "PROD-001",
                    "variant_id": 0,
                    "name": "Product Name",
                    "attributes": "Size: L, Color: Blue",
                    "sku": "SKU-001",
                    "ean": "1234567890123",
                    "location": "A1-B2",
                    "warehouse_id": 0,
                    "auction_id": "",
                    "price_brutto": 29.99,
                    "tax_rate": 23,
                    "quantity": 2,
                    "weight": 0.5
                }
            ]
        }
    ]
}
```

### add_order(**kwargs)

Add new order to BaseLinker order manager.

**Required Parameters:**
- `order_source_id` (int): Order source identifier
- `date_add` (int): Order creation timestamp (Unix)
- `order_status_id` (int): Order status

**Optional Parameters:**
- `currency` (char(3)): 3-letter currency code (e.g., "PLN", "EUR", "USD")
- `payment_method` (varchar(30)): Payment method name
- `payment_method_cod` (bool): Cash on delivery flag
- `payment_done` (float): Payment amount received
- `delivery_method` (varchar(30)): Shipping method name
- `delivery_price` (float): Gross delivery price
- `delivery_package_module` (varchar(20)): Delivery package module
- `delivery_package_nr` (varchar(50)): Package tracking number
- `delivery_fullname` (varchar(100)): Delivery recipient name
- `delivery_company` (varchar(100)): Delivery company name
- `delivery_address` (varchar(100)): Delivery street address
- `delivery_city` (varchar(50)): Delivery city
- `delivery_postcode` (varchar(20)): Delivery postal code
- `delivery_country_code` (char(2)): Delivery country (2-letter code)
- `delivery_point_id` (varchar(40)): Delivery point identifier
- `delivery_point_name` (varchar(100)): Delivery point name
- `delivery_point_address` (varchar(100)): Delivery point address
- `delivery_point_postcode` (varchar(20)): Delivery point postal code
- `delivery_point_city` (varchar(50)): Delivery point city
- `invoice_fullname` (varchar(100)): Invoice recipient name
- `invoice_company` (varchar(100)): Invoice company name
- `invoice_nip` (varchar(20)): Tax identification number
- `invoice_address` (varchar(100)): Invoice address
- `invoice_city` (varchar(50)): Invoice city
- `invoice_postcode` (varchar(20)): Invoice postal code
- `invoice_country_code` (char(2)): Invoice country (2-letter code)
- `want_invoice` (bool): Invoice required flag
- `user_comments` (text): Customer comments
- `admin_comments` (text): Admin comments
- `email` (varchar(150)): Customer email
- `phone` (varchar(50)): Customer phone
- `user_login` (varchar(50)): Customer login
- `products` (array): Array of order products

**Product Structure:**
```json
{
    "storage": "bl|shop|warehouse",
    "storage_id": 0,
    "product_id": "PROD-001",
    "variant_id": 0,
    "name": "Product Name",
    "attributes": "Size: L",
    "sku": "SKU-001",
    "ean": "1234567890123",
    "location": "A1",
    "warehouse_id": 0,
    "auction_id": "",
    "price_brutto": 29.99,
    "tax_rate": 23,
    "quantity": 1,
    "weight": 0.5
}
```

**Returns:**
```json
{
    "status": "SUCCESS",
    "order_id": 12345
}
```

### get_order_sources()

Retrieve list of order sources.

**Parameters:** None

**Returns:**
```json
{
    "status": "SUCCESS",
    "sources": [
        {
            "id": 1,
            "name": "My Shop",
            "source": "shop"
        }
    ]
}
```

### set_order_fields(**kwargs)

Edit specific fields of an existing order.

**Required Parameters:**
- `order_id` (int): Order identifier

**Optional Parameters:**
- `admin_comments` (text): Admin comments
- `user_comments` (text): Customer comments
- `payment_method` (varchar(30)): Payment method
- `payment_method_cod` (bool): Cash on delivery
- `payment_done` (float): Payment amount
- `delivery_method` (varchar(30)): Delivery method
- `delivery_price` (float): Delivery price
- `delivery_fullname` (varchar(100)): Delivery name
- `delivery_company` (varchar(100)): Delivery company
- `delivery_address` (varchar(100)): Delivery address
- `delivery_city` (varchar(50)): Delivery city
- `delivery_postcode` (varchar(20)): Delivery postcode
- `delivery_country_code` (char(2)): Delivery country
- `phone` (varchar(50)): Phone number
- `email` (varchar(150)): Email address
- `pick_state` (int): Pick state
- `pack_state` (int): Pack state

### set_order_status(**kwargs)

Change order status.

**Required Parameters:**
- `order_id` (int): Order identifier
- `status_id` (int): New status identifier

### add_order_product(**kwargs)

Add product to existing order.

**Required Parameters:**
- `order_id` (int): Order identifier
- `product_id` (varchar(30)): Product identifier
- `name` (varchar(200)): Product name
- `price_brutto` (float): Gross price
- `tax_rate` (float): Tax rate (0-100)
- `quantity` (int): Quantity

**Optional Parameters:**
- `storage` (varchar(20)): Storage type (bl/shop/warehouse)
- `storage_id` (int): Storage identifier
- `variant_id` (int): Product variant ID
- `attributes` (varchar(50)): Product attributes
- `sku` (varchar(50)): SKU code
- `ean` (varchar(20)): EAN code
- `location` (varchar(10)): Storage location
- `warehouse_id` (int): Warehouse identifier
- `auction_id` (varchar(20)): Auction identifier
- `weight` (float): Product weight

### set_order_product_fields(**kwargs)

Edit order product fields.

**Required Parameters:**
- `order_id` (int): Order identifier
- `order_product_id` (int): Order product identifier

**Optional Parameters:**
- `name` (varchar(200)): Product name
- `attributes` (varchar(50)): Product attributes
- `sku` (varchar(50)): SKU code
- `ean` (varchar(20)): EAN code
- `location` (varchar(10)): Storage location
- `warehouse_id` (int): Warehouse identifier
- `auction_id` (varchar(20)): Auction identifier
- `price_brutto` (float): Gross price
- `tax_rate` (float): Tax rate
- `quantity` (int): Quantity
- `weight` (float): Product weight

### delete_order_product(**kwargs)

Delete product from order.

**Required Parameters:**
- `order_id` (int): Order identifier
- `order_product_id` (int): Order product identifier

### get_journal_list(**kwargs)

Get journal/log entries for orders.

**Optional Parameters:**
- `last_log_id` (int): Last log ID for pagination
- `logs_types` (array): Filter by log types
- `order_id` (int): Filter by specific order

### get_order_transaction_data(**kwargs)

Get order transaction data.

**Required Parameters:**
- `order_id` (int): Order identifier

### get_order_payments_history(**kwargs)

Get order payments history.

**Required Parameters:**
- `order_id` (int): Order identifier

## Product Catalog Methods

### get_inventories()

Get list of BaseLinker catalogs.

**Parameters:** None

**Returns:**
```json
{
    "status": "SUCCESS",
    "inventories": [
        {
            "inventory_id": 123,
            "name": "Main Catalog",
            "description": "Primary product catalog",
            "languages": ["pl", "en"],
            "default_language": "pl",
            "price_groups": [1, 2, 3],
            "default_price_group": 1,
            "warehouses": ["bl_123"],
            "default_warehouse": "bl_123",
            "reservations": true
        }
    ]
}
```

### get_inventory_products_list(**kwargs)

Get products list from BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier

**Optional Parameters:**
- `filter_category_id` (int): Filter by category
- `filter_limit` (int): Results limit (max 1000, default 1000)
- `filter_offset` (int): Results offset for pagination
- `filter_sort` (varchar(20)): Sort field (id/name/quantity/price)
- `filter_id` (varchar(30)): Filter by product ID
- `filter_ean` (varchar(20)): Filter by EAN
- `filter_sku` (varchar(50)): Filter by SKU
- `filter_name` (varchar(100)): Filter by product name
- `filter_price_from` (float): Minimum price
- `filter_price_to` (float): Maximum price
- `filter_quantity_from` (int): Minimum quantity
- `filter_quantity_to` (int): Maximum quantity
- `filter_available` (int): Filter by availability (0=all, 1=available, 2=unavailable)

**Returns:**
```json
{
    "status": "SUCCESS",
    "products": [
        {
            "id": "PROD-001",
            "ean": "1234567890123",
            "sku": "SKU-001",
            "name": "Product Name",
            "quantity": 100,
            "price_netto": 24.39,
            "price_brutto": 29.99,
            "price_wholesale_netto": 20.33,
            "price_wholesale_brutto": 25.00,
            "tax_rate": 23,
            "weight": 0.5,
            "description": "Product description",
            "description_extra1": "Additional info",
            "description_extra2": "Technical specs",
            "description_extra3": "Warranty info",
            "description_extra4": "Usage instructions",
            "man_name": "Manufacturer",
            "man_image": "manufacturer_logo.jpg",
            "category_id": 1,
            "images": [
                {
                    "url": "https://example.com/image1.jpg",
                    "title": "Main image",
                    "sort": 1
                }
            ],
            "features": [
                {
                    "name": "Color",
                    "value": "Blue"
                }
            ]
        }
    ]
}
```

### get_inventory_products_data(**kwargs)

Get detailed products data from BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `products` (array): Array of product IDs to retrieve

**Returns:** Detailed product data including all text fields, images, variants, bundles, and related products.

### add_inventory_product(**kwargs)

Add or update product in BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `product_id` (varchar(30)): Product identifier

**Optional Parameters:**
- `parent_id` (varchar(30)): Parent product ID for variants
- `is_bundle` (bool): Bundle product flag
- `ean` (varchar(20)): EAN code
- `sku` (varchar(50)): SKU code
- `tax_rate` (float): VAT tax rate (0-100)
- `weight` (float): Product weight in kg
- `width` (float): Product width in cm
- `height` (float): Product height in cm
- `length` (float): Product length in cm
- `star` (int): Star rating (0-5)
- `manufacturer_id` (int): Manufacturer identifier
- `category_id` (int): Category identifier
- `prices` (object): Price groups data
- `stock` (object): Warehouse stock levels
- `locations` (object): Warehouse locations
- `text_fields` (object): Multilingual text content
- `images` (array): Product images
- `links` (array): Related links

**Price Groups Structure:**
```json
{
    "1": {
        "price_netto": 24.39,
        "price_brutto": 29.99,
        "price_wholesale_netto": 20.33,
        "price_wholesale_brutto": 25.00
    }
}
```

**Stock Structure:**
```json
{
    "bl_123": 100,
    "shop_456": 50
}
```

**Text Fields Structure:**
```json
{
    "name": "Product Name",
    "description": "Product description",
    "description_extra1": "Additional description",
    "description_extra2": "Technical specifications",
    "description_extra3": "Warranty information",
    "description_extra4": "Usage instructions",
    "man_name": "Manufacturer Name",
    "man_image": "manufacturer_logo.jpg"
}
```

### delete_inventory_product(**kwargs)

Delete product from BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `product_id` (varchar(30)): Product identifier

### update_inventory_products_stock(**kwargs)

Update product stock levels in BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `products` (array): Array of stock updates

**Product Stock Structure:**
```json
{
    "product_id": "PROD-001",
    "variant_id": 0,
    "stock": {
        "bl_123": 100,
        "shop_456": 50
    }
}
```

**Limitations:** Maximum 1000 products per request

### update_inventory_products_prices(**kwargs)

Update product prices in BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `products` (array): Array of price updates

**Product Price Structure:**
```json
{
    "product_id": "PROD-001",
    "variant_id": 0,
    "price_netto": 24.39,
    "price_brutto": 29.99,
    "price_wholesale_netto": 20.33,
    "price_wholesale_brutto": 25.00
}
```

### get_inventory_categories(**kwargs)

Get categories from BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier

**Returns:**
```json
{
    "status": "SUCCESS",
    "categories": [
        {
            "category_id": 1,
            "name": "Electronics",
            "parent_id": 0,
            "sort": 1
        }
    ]
}
```

### add_inventory_category(**kwargs)

Add category to BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `name` (varchar(100)): Category name

**Optional Parameters:**
- `parent_id` (int): Parent category ID (0 for root)
- `sort` (int): Sort order

### delete_inventory_category(**kwargs)

Delete category from BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `category_id` (int): Category identifier

### add_inventory(**kwargs)

Create new BaseLinker catalog.

**Required Parameters:**
- `name` (varchar(100)): Catalog name

**Optional Parameters:**
- `description` (text): Catalog description
- `languages` (array): Available languages
- `default_language` (char(2)): Default language
- `price_groups` (array): Price group identifiers
- `default_price_group` (int): Default price group
- `warehouses` (array): Warehouse identifiers
- `default_warehouse` (varchar(30)): Default warehouse
- `reservations` (bool): Reservation support

### delete_inventory(**kwargs)

Delete BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier

## Inventory Management Methods

### get_inventory_warehouses(**kwargs)

Get warehouses from BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier

**Returns:**
```json
{
    "status": "SUCCESS",
    "warehouses": [
        {
            "warehouse_id": "bl_123",
            "name": "Main Warehouse",
            "description": "Primary storage location",
            "stock_edition": true,
            "is_default": true,
            "disable_stock_level_below_zero": false
        }
    ]
}
```

### add_inventory_warehouse(**kwargs)

Add warehouse to BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `warehouse_id` (varchar(30)): Warehouse identifier
- `name` (varchar(100)): Warehouse name

**Optional Parameters:**
- `description` (text): Warehouse description
- `stock_edition` (bool): Allow stock editing
- `is_default` (bool): Default warehouse flag
- `disable_stock_level_below_zero` (bool): Prevent negative stock

### delete_inventory_warehouse(**kwargs)

Delete warehouse from BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `warehouse_id` (varchar(30)): Warehouse identifier

### get_inventory_price_groups(**kwargs)

Get price groups from BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier

**Returns:**
```json
{
    "status": "SUCCESS",
    "price_groups": [
        {
            "price_group_id": 1,
            "name": "Retail",
            "description": "Standard retail prices",
            "currency": "PLN",
            "is_default": true
        }
    ]
}
```

### add_inventory_price_group(**kwargs)

Add price group to BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `price_group_id` (int): Price group identifier
- `name` (varchar(100)): Price group name

**Optional Parameters:**
- `description` (text): Price group description
- `currency` (char(3)): Currency code
- `is_default` (bool): Default price group flag

### delete_inventory_price_group(**kwargs)

Delete price group from BaseLinker catalog.

**Required Parameters:**
- `inventory_id` (int): Catalog identifier
- `price_group_id` (int): Price group identifier

## Courier & Shipping Methods

### get_couriers_list()

Get list of available couriers.

**Parameters:** None

**Returns:**
```json
{
    "status": "SUCCESS",
    "couriers": [
        {
            "courier_code": "dpd",
            "name": "DPD",
            "services": ["standard", "express", "cod"],
            "countries": ["PL", "DE", "FR"]
        }
    ]
}
```

### create_package(**kwargs)

Create shipment package in courier system.

**Required Parameters:**
- `order_id` (int): Order identifier
- `courier_code` (varchar(20)): Courier code (e.g., "dpd", "ups", "fedex")

**Optional Parameters:**
- `account_id` (int): Courier API account identifier
- `fields` (object): Courier-specific form fields
- `packages` (array): Package details

**Package Structure:**
```json
{
    "size": "M",
    "weight": 2.5,
    "width": 30,
    "height": 20,
    "length": 40,
    "declared_content": "Electronics",
    "insurance": true,
    "insurance_value": 299.99,
    "cod_amount": 299.99,
    "delivery_confirmation": true
}
```

**Returns:**
```json
{
    "status": "SUCCESS",
    "package_id": 12345,
    "package_number": "PKG123456789",
    "courier_inner_number": "DPD987654321",
    "tracking_number": "1234567890"
}
```

### create_package_manual(**kwargs)

Manually create package with tracking number.

**Required Parameters:**
- `order_id` (int): Order identifier
- `courier_code` (varchar(20)): Courier code
- `package_number` (varchar(50)): Tracking/package number

**Optional Parameters:**
- `pickup_date` (varchar(10)): Pickup date (YYYY-MM-DD)
- `return_shipment` (bool): Return shipment flag

### get_label(**kwargs)

Download shipping label.

**Required Parameters:**
- `package_id` (int): Package identifier

**Optional Parameters:**
- `label_format` (varchar(10)): Label format ("PDF", "ZPL", "EPL")
- `label_size` (varchar(20)): Label size ("100x150mm", "A4")

**Returns:**
```json
{
    "status": "SUCCESS",
    "label": "base64_encoded_label_data...",
    "label_format": "PDF",
    "label_size": "100x150mm"
}
```

### get_order_packages(**kwargs)

Get packages for specific order.

**Required Parameters:**
- `order_id` (int): Order identifier

**Returns:**
```json
{
    "status": "SUCCESS",
    "packages": [
        {
            "package_id": 12345,
            "package_number": "PKG123456789",
            "courier_code": "dpd",
            "status": "created",
            "tracking_number": "1234567890",
            "pickup_date": "2024-01-15",
            "return_shipment": false
        }
    ]
}
```

### request_parcel_pickup(**kwargs)

Request parcel pickup from courier.

**Required Parameters:**
- `courier_code` (varchar(20)): Courier code
- `package_ids` (array): Array of package IDs
- `pickup_date` (varchar(10)): Pickup date (YYYY-MM-DD)

**Optional Parameters:**
- `pickup_time_from` (varchar(5)): Pickup time from (HH:MM)
- `pickup_time_to` (varchar(5)): Pickup time to (HH:MM)
- `address` (object): Pickup address

**Address Structure:**
```json
{
    "name": "Company Name",
    "company": "ACME Corp",
    "street": "Main Street 123",
    "city": "Warsaw",
    "postcode": "00-001",
    "country": "PL",
    "phone": "+48123456789",
    "email": "pickup@company.com"
}
```

## External Storage Methods

### get_external_storages_list()

Get list of external storage connections.

**Parameters:** None

**Returns:**
```json
{
    "status": "SUCCESS",
    "storages": [
        {
            "storage_id": "allegro_123",
            "name": "Allegro Store",
            "type": "allegro",
            "status": "active",
            "url": "https://allegro.pl/shop/123"
        }
    ]
}
```

### get_external_storage_products_data(**kwargs)

Get detailed product data from external storage.

**Required Parameters:**
- `storage_id` (varchar(30)): External storage identifier
- `products` (array): Array of product IDs

**Returns:** Detailed product information from external marketplace.

### get_external_storage_products_quantity(**kwargs)

Get product stock quantities from external storage.

**Required Parameters:**
- `storage_id` (varchar(30)): External storage identifier
- `products` (array): Array of product IDs

**Returns:**
```json
{
    "status": "SUCCESS",
    "products": [
        {
            "product_id": "EXT123",
            "variants": [
                {
                    "variant_id": "VAR1",
                    "stock": 15
                }
            ]
        }
    ]
}
```

### update_external_storage_products_quantity(**kwargs)

Update product stock quantities in external storage.

**Required Parameters:**
- `storage_id` (varchar(30)): External storage identifier
- `products` (array): Array of products with stock updates

**Product Structure:**
```json
{
    "product_id": "EXT123",
    "variants": [
        {
            "variant_id": "VAR1",
            "stock": 20
        }
    ]
}
```

**Limitations:** Maximum 1000 products per request

## Order Returns Methods

### add_order_return(**kwargs)

Add new order return.

**Required Parameters:**
- `order_id` (int): Order identifier
- `return_status` (int): Return status identifier
- `products` (array): Array of returned products

**Optional Parameters:**
- `return_reason` (varchar(100)): Return reason
- `admin_comments` (text): Admin comments
- `return_address` (object): Return address
- `refund_amount` (float): Refund amount
- `refund_method` (varchar(50)): Refund method

**Product Structure:**
```json
{
    "order_product_id": 456,
    "quantity": 1,
    "reason": "Damaged item",
    "refund_amount": 29.99
}
```

**Returns:**
```json
{
    "status": "SUCCESS",
    "return_id": 12345
}
```

### get_order_returns(**kwargs)

Get order returns from specific date.

**Optional Parameters:**
- `date_confirmed_from` (int): Unix timestamp - confirmed returns from this date
- `date_from` (int): Unix timestamp - returns created from this date
- `date_to` (int): Unix timestamp - returns created until this date
- `return_status` (int): Filter by return status
- `order_id` (int): Filter by specific order
- `get_unconfirmed_returns` (bool): Include unconfirmed returns

**Limitations:** Maximum 100 returns per request

**Returns:**
```json
{
    "status": "SUCCESS",
    "returns": [
        {
            "return_id": 12345,
            "order_id": 123,
            "return_status": 1,
            "return_reason": "Damaged item",
            "date_add": 1640995200,
            "date_confirmed": 1640995800,
            "admin_comments": "Return approved",
            "refund_amount": 29.99,
            "refund_method": "Credit Card",
            "products": [
                {
                    "order_product_id": 456,
                    "quantity": 1,
                    "reason": "Item arrived damaged",
                    "refund_amount": 29.99
                }
            ]
        }
    ]
}
```

### set_order_return_fields(**kwargs)

Edit order return fields.

**Required Parameters:**
- `return_id` (int): Return identifier

**Optional Parameters:**
- `admin_comments` (text): Admin comments
- `return_reason` (varchar(100)): Return reason
- `refund_amount` (float): Refund amount
- `refund_method` (varchar(50)): Refund method

### set_order_return_status(**kwargs)

Change order return status.

**Required Parameters:**
- `return_id` (int): Return identifier
- `return_status` (int): New return status identifier

## Response Formats

### Success Response
All successful API calls return:
```json
{
    "status": "SUCCESS",
    // Method-specific data
}
```

### Error Response
Error responses include:
```json
{
    "status": "ERROR",
    "error_code": "ERROR_AUTH_TOKEN",
    "error_message": "Invalid authentication token"
}
```

### Common Response Fields
- `status`: "SUCCESS" or "ERROR"
- `error_code`: Error identifier (when status is ERROR)
- `error_message`: Human-readable error description
- `warnings`: Array of warning messages (optional)

## Error Handling

### Common Error Codes
- `ERROR_AUTH_TOKEN`: Invalid or missing authentication token
- `ERROR_RATE_LIMIT`: API rate limit exceeded (100 requests/minute)
- `ERROR_INVALID_PARAMETERS`: Invalid or missing required parameters
- `ERROR_NOT_FOUND`: Requested resource not found
- `ERROR_PERMISSION_DENIED`: Insufficient permissions
- `ERROR_TEMPORARY`: Temporary server error (retry recommended)
- `ERROR_SERVER`: Internal server error

### Rate Limiting
- **Limit**: 100 requests per minute
- **Reset**: Rate limit resets every minute
- **Headers**: No rate limit headers provided
- **Handling**: Wait 60 seconds when rate limit exceeded

### Best Practices
1. Always check `status` field in response
2. Implement exponential backoff for retries
3. Handle rate limits gracefully
4. Log error codes for debugging
5. Validate parameters before sending requests
6. Use batch operations when available
7. Cache frequently accessed data

### Parameter Validation
- **Required fields**: Must be provided for request to succeed
- **Data types**: Strictly enforced (int, float, varchar, text, bool)
- **Length limits**: Varchar fields have maximum character limits
- **Value ranges**: Some fields have specific value constraints
- **Encoding**: UTF-8 encoding required for all text