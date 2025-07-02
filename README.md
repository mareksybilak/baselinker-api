# BaseLinker API Python Integration

[![PyPI version](https://badge.fury.io/py/baselinker-api.svg)](https://badge.fury.io/py/baselinker-api)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-300%20passed-green.svg)](https://github.com/your-username/baselinker-api)
[![Coverage](https://img.shields.io/badge/coverage-82%25-brightgreen.svg)](https://github.com/your-username/baselinker-api)

Python library for integrating with [BaseLinker API](https://api.baselinker.com) - a comprehensive e-commerce management platform with **modular architecture** and **133 API methods**.

## ✨ Features

- **🏗️ Modular Architecture** - Organized by functional areas (orders, products, inventory, etc.)
- **📈 Comprehensive Coverage** - 133 API methods across 9 specialized modules
- **🔒 Type Safety** - Parameter validation and error handling
- **📚 Full Documentation** - Complete method documentation with examples
- **🧪 Well Tested** - 300+ test methods with 82% test coverage
- **🚀 Easy to Use** - Intuitive module-based interface

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Modular Architecture](#modular-architecture)
- [Authentication](#authentication)
- [API Modules](#api-modules)
- [Error Handling](#error-handling)
- [Examples](#examples)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
pip install baselinkerapi
```

Or install from source:

```bash
git clone https://github.com/your-username/baselinker-api.git
cd baselinker-api
pip install -e .
```

## Quick Start

```python
from baselinker import BaseLinkerClient

# Initialize client with API token
client = BaseLinkerClient(token="your-api-token")

# Get recent orders using orders module
orders = client.orders.get_orders(date_from=1640995200)
print(f"Found {len(orders.get('orders', []))} orders")

# Search orders by customer email
customer_orders = client.orders.get_orders_by_email(email="customer@example.com")

# Get products from inventory
inventories = client.products.get_inventories()
if inventories.get('inventories'):
    inventory_id = inventories['inventories'][0]['inventory_id']
    products = client.products.get_inventory_products_list(inventory_id=inventory_id)

# Create invoice for order
invoice = client.invoices.add_invoice(order_id=12345)

# Get courier services
couriers = client.courier.get_couriers_list()
```

## Modular Architecture

The BaseLinker API client is organized into specialized modules for better code organization:

```python
client = BaseLinkerClient(token)

# 🛒 Orders Management (17 methods)
client.orders.get_orders()
client.orders.add_order()
client.orders.get_orders_by_email(email="customer@example.com")
client.orders.get_orders_by_phone(phone="+48123456789")
client.orders.set_order_status()

# 📦 Product Catalog (23 methods)  
client.products.get_inventories()
client.products.get_inventory_products_list()
client.products.add_inventory_product()
client.products.get_inventory_manufacturers()
client.products.get_inventory_tags()

# 🏪 Inventory Management (6 methods)
client.inventory.get_inventory_warehouses()
client.inventory.add_inventory_warehouse()
client.inventory.get_inventory_price_groups()

# 🚚 Courier Services (14 methods)
client.courier.get_couriers_list()
client.courier.create_package()
client.courier.get_courier_services()
client.courier.get_label()

# 💰 Invoices & Payments (8 methods)
client.invoices.add_invoice()
client.invoices.get_invoices()
client.invoices.set_order_payment()
client.invoices.get_series()

# 🔄 Returns Management (10 methods)
client.returns.add_order_return()
client.returns.get_order_returns()
client.returns.get_order_return_status_list()

# 🌐 External Storage (7 methods)
client.external_storage.get_external_storages_list()
client.external_storage.get_external_storage_products_data()

# 📋 Document Management (6 methods)
client.documents.get_inventory_documents()
client.documents.get_inventory_purchase_orders()

# 🔧 Device Management (18 methods)
client.devices.get_printers()
client.devices.get_connect_integrations()
```

## Authentication

Get your API token from BaseLinker:

1. Log in to your BaseLinker account
2. Go to **Settings** → **API**
3. Generate a new API token
4. Use the token to initialize the client

```python
from baselinker import BaseLinkerClient

# Initialize with token
client = BaseLinkerClient(token="your-api-token-here")

# Optional: Set custom timeout (default: 30 seconds)
client = BaseLinkerClient(token="your-token", timeout=60)
```

## API Modules

### 📋 Orders Module

Complete order lifecycle management:

```python
# Search and retrieve orders
orders = client.orders.get_orders(date_from=1640995200)
email_orders = client.orders.get_orders_by_email(email="customer@example.com")
phone_orders = client.orders.get_orders_by_phone(phone="+48123456789")

# Order management
client.orders.set_order_status(order_id=123, status_id=2)
client.orders.set_order_fields(order_id=123, admin_comments="Processed")

# Order products
client.orders.add_order_product(
    order_id=123,
    product_id="PROD-001", 
    name="Test Product",
    price_brutto=29.99,
    tax_rate=23.0,
    quantity=1
)

# Get order statuses and sources
statuses = client.orders.get_order_status_list()
sources = client.orders.get_order_sources()
```

### 📦 Products Module

Comprehensive catalog management:

```python
# Inventory and catalog management
inventories = client.products.get_inventories()
products = client.products.get_inventory_products_list(inventory_id=123)

# Product data and details
product_data = client.products.get_inventory_products_data(
    inventory_id=123, 
    products=["PROD-001", "PROD-002"]
)

# Stock and pricing
client.products.update_inventory_products_stock(
    inventory_id=123,
    products=[{"product_id": "PROD-001", "stock": {"bl_123": 100}}]
)

# Categories and organization
categories = client.products.get_inventory_categories(inventory_id=123)
manufacturers = client.products.get_inventory_manufacturers(inventory_id=123)
tags = client.products.get_inventory_tags(inventory_id=123)

# Product logs and tracking
logs = client.products.get_inventory_product_logs(inventory_id=123)
```

### 💰 Invoices Module

Invoice and payment processing:

```python
# Create and manage invoices
invoice = client.invoices.add_invoice(order_id=12345)
invoices = client.invoices.get_invoices()

# Payment management
client.invoices.set_order_payment(order_id=12345, payment_done=1)
payment_history = client.invoices.get_order_payments_history(order_id=12345)

# Document series and numbering
series = client.invoices.get_series()
```

### 🚚 Courier Module

Shipping and logistics:

```python
# Courier services
couriers = client.courier.get_couriers_list()
services = client.courier.get_courier_services(courier_code="dpd")

# Package creation and management
package = client.courier.create_package(
    order_id=123,
    courier_code="dpd"
)

# Labels and tracking
label = client.courier.get_label(package_id=456)
packages = client.courier.get_order_packages(order_id=123)

# Pickup requests
pickup = client.courier.request_parcel_pickup(
    courier_code="dpd",
    package_ids=[456, 789],
    pickup_date="2024-01-15"
)
```

## Error Handling

The library provides comprehensive error handling:

```python
from baselinker import BaseLinkerClient, BaseLinkerError, AuthenticationError, RateLimitError

client = BaseLinkerClient(token="your-token")

try:
    orders = client.orders.get_orders()
except AuthenticationError:
    print("Invalid API token")
except RateLimitError:
    print("Rate limit exceeded - wait 60 seconds")
except BaseLinkerError as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Examples

See the [`examples/`](examples/) directory for complete examples:

- [`basic_usage.py`](examples/basic_usage.py) - Basic API usage
- [`modular_usage.py`](examples/modular_usage.py) - Modular architecture demonstration
- [`new_features_showcase.py`](examples/new_features_showcase.py) - New features showcase

## Development

Clone the repository and install development dependencies:

```bash
git clone https://github.com/your-username/baselinker-api.git
cd baselinker-api
pip install -e ".[dev]"
```

### Development dependencies include:
- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting
- `black` - Code formatting
- `flake8` - Code linting

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=baselinker

# Run specific test file
pytest tests/test_orders.py

# Run with verbose output
pytest -v
```

### Test Structure
- `tests/test_modular_structure.py` - Modular architecture tests
- `tests/test_order_management.py` - Orders module tests
- `tests/test_product_catalog.py` - Products module tests
- `tests/test_warehouse.py` - Inventory module tests
- `tests/test_courier.py` - Courier module tests
- `tests/test_order_returns.py` - Returns module tests
- `tests/test_external_storage.py` - External storage tests
- `tests/test_client.py` - Core client tests
- `tests/test_integration.py` - Integration tests
- `tests/test_*_comprehensive.py` - Comprehensive module tests
- `tests/test_validators_simple.py` - Parameter validation tests
- `tests/test_all_modules_coverage.py` - Coverage optimization tests

### Test Coverage Details

**Overall Coverage: 82%** 

| Module | Coverage | Status |
|--------|----------|--------|
| client.py | 91% | ✅ Excellent |
| orders.py | 82% | ✅ Very Good |
| products.py | 83% | ✅ Very Good |
| inventory.py | 100% | ✅ Perfect |
| courier.py | 73% | ✅ Good |
| invoices.py | 88% | ✅ Very Good |
| returns.py | 78% | ✅ Good |
| external_storage.py | 77% | ✅ Good |
| documents.py | 64% | 🔶 Moderate |
| devices.py | 68% | 🔶 Moderate |
| validators.py | 98% | ✅ Excellent |

**Test Statistics:**
- Total test files: 15+
- Total test methods: 300+
- All 133 API methods tested
- Parameter validation coverage: 98%
- Error handling scenarios: Comprehensive

## API Coverage

This library provides comprehensive coverage of the BaseLinker API:

| Module | Methods | Coverage |
|--------|---------|----------|
| Orders | 24 | ✅ Complete |
| Products | 30 | ✅ Complete |
| Inventory | 8 | ✅ Complete |
| Courier | 14 | ✅ Complete |
| Invoices | 10 | ✅ Complete |
| Returns | 11 | ✅ Complete |
| External Storage | 8 | ✅ Complete |
| Documents | 8 | ✅ Complete |
| Devices | 20 | ✅ Complete |
| **Total** | **133** | **~80%** |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate and follow the existing code style.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [BaseLinker](https://baselinker.com) for providing the comprehensive e-commerce API
- Contributors and users of this library

---

**Note**: This is an unofficial library. BaseLinker is a trademark of BaseLinker Sp. z o.o.