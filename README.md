# BaseLinker API Python Integration

[![PyPI version](https://badge.fury.io/py/baselinker-api.svg)](https://badge.fury.io/py/baselinker-api)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-62%20passed-green.svg)](https://github.com/your-username/baselinker-api)
[![Coverage](https://img.shields.io/badge/coverage-94%25-brightgreen.svg)](https://github.com/your-username/baselinker-api)

Python library for integrating with [BaseLinker API](https://api.baselinker.com) - a comprehensive e-commerce management platform.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Authentication](#authentication)
- [API Methods](#api-methods)
- [Error Handling](#error-handling)
- [Examples](#examples)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
pip install baselinker-api
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

# Get recent orders
orders = client.get_orders(date_from=1640995200)
print(f"Found {len(orders.get('orders', []))} orders")

# Add product to inventory
product = client.add_inventory_product(
    inventory_id=123,
    product_id="ABC123",
    name="Sample Product",
    price_netto=29.99,
    price_brutto=36.89,
    tax_rate=23
)
print(f"Product added with ID: {product.get('product_id')}")
```

## Authentication

Get your API token from BaseLinker account:

1. Log in to your BaseLinker account
2. Go to **Settings** → **API**
3. Generate new API token
4. Use the token in your application

### Environment Variable

You can store your token in environment variable:

```bash
export BASELINKER_TOKEN="your-api-token"
```

```python
import os
from baselinker import BaseLinkerClient

token = os.getenv('BASELINKER_TOKEN')
client = BaseLinkerClient(token)
```

## API Methods

### Order Management

```python
# Get orders
orders = client.get_orders(date_from=1640995200, get_unconfirmed_orders=True)

# Add new order
order = client.add_order(
    order_source_id=1,
    delivery_price=15.99,
    user_comments="Test order"
)

# Update order status
client.set_order_status(order_id=123, status_id=2)

# Add product to order
client.add_order_product(
    order_id=123,
    product_id="ABC123",
    name="Product Name",
    quantity=2,
    price=29.99
)

# Get order sources
sources = client.get_order_sources()
```

### Product Catalog

```python
# Get inventories
inventories = client.get_inventories()

# Get products list
products = client.get_inventory_products_list(
    inventory_id=123,
    filter_name="laptop"
)

# Get detailed product data
product_data = client.get_inventory_products_data(
    inventory_id=123,
    products=["ABC123", "DEF456"]
)

# Update product stock
client.update_inventory_products_stock(
    inventory_id=123,
    products=[
        {"product_id": "ABC123", "variant_id": 0, "stock": 50}
    ]
)

# Update product prices
client.update_inventory_products_prices(
    inventory_id=123,
    products=[
        {
            "product_id": "ABC123",
            "variant_id": 0,
            "price_netto": 24.99,
            "price_brutto": 30.74
        }
    ]
)
```

### Warehouse Management

```python
# Get warehouses
warehouses = client.get_inventory_warehouses(inventory_id=123)

# Add new warehouse
warehouse = client.add_inventory_warehouse(
    inventory_id=123,
    name="New Warehouse",
    description="Additional storage facility"
)

# Get price groups
price_groups = client.get_inventory_price_groups(inventory_id=123)
```

### Courier & Shipping

```python
# Get available couriers
couriers = client.get_couriers_list()

# Create package
package = client.create_package(
    order_id=123,
    courier_code="DPD",
    fields={
        "size": "M",
        "weight": 2.5
    }
)

# Get shipping label
label = client.get_label(package_id=789)

# Request parcel pickup
pickup = client.request_parcel_pickup(
    courier_code="DPD",
    package_ids=[789, 790],
    pickup_date="2023-12-01"
)
```

### External Storage

```python
# Get external storages
storages = client.get_external_storages_list()

# Get products from external storage
products = client.get_external_storage_products_data(
    storage_id="allegro_123"
)

# Update quantities in external storage
client.update_external_storage_products_quantity(
    storage_id="allegro_123",
    products=[
        {
            "product_id": "EXT123",
            "variants": [{"variant_id": "VAR1", "stock": 20}]
        }
    ]
)
```

### Order Returns

```python
# Add order return
return_obj = client.add_order_return(
    order_id=123,
    return_reason="Damaged item",
    products=[
        {
            "order_product_id": 456,
            "quantity": 1,
            "reason": "Item arrived damaged"
        }
    ]
)

# Get returns
returns = client.get_order_returns(date_from=1640995200)

# Update return status
client.set_order_return_status(return_id=12345, return_status=3)
```

## Error Handling

The library provides specific exceptions for different error types:

```python
from baselinker import BaseLinkerClient
from baselinker.exceptions import (
    AuthenticationError,
    RateLimitError,
    APIError,
    BaseLinkerError
)

client = BaseLinkerClient("your-token")

try:
    orders = client.get_orders()
except AuthenticationError:
    print("Invalid API token")
except RateLimitError:
    print("Rate limit exceeded - wait before retry")
except APIError as e:
    print(f"API error: {e} (code: {e.error_code})")
except BaseLinkerError as e:
    print(f"General error: {e}")
```

## Rate Limiting

BaseLinker API has a rate limit of **100 requests per minute**. The library will raise `RateLimitError` when this limit is exceeded.

```python
import time
from baselinker.exceptions import RateLimitError

def safe_api_call(client, method, **kwargs):
    try:
        return getattr(client, method)(**kwargs)
    except RateLimitError:
        print("Rate limit hit, waiting 60 seconds...")
        time.sleep(60)
        return getattr(client, method)(**kwargs)
```

## Examples

See the [examples/](examples/) directory for complete examples:

- [basic_usage.py](examples/basic_usage.py) - Basic API usage
- [product_management.py](examples/product_management.py) - Product catalog management

## Development

### Setup Development Environment

```bash
git clone https://github.com/your-username/baselinker-api.git
cd baselinker-api
pip install -e ".[dev]"
```

### Project Structure

```
baselinker-api/
├── baselinker/
│   ├── __init__.py
│   ├── client.py          # Main API client
│   └── exceptions.py      # Custom exceptions
├── tests/
│   ├── test_client.py     # Basic client tests
│   ├── test_order_management.py
│   ├── test_product_catalog.py
│   ├── test_warehouse.py
│   ├── test_courier.py
│   ├── test_external_storage.py
│   ├── test_order_returns.py
│   └── test_integration.py
├── examples/
│   ├── basic_usage.py
│   └── product_management.py
└── README.md
```

## Testing

Run tests:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=baselinker --cov-report=term-missing

# Run specific test file
pytest tests/test_client.py -v
```

Current test coverage: **94%** (62 tests passing)

### Test Categories

- **Unit tests**: Test individual methods and error handling
- **Integration tests**: Test complete workflows
- **Mock tests**: All tests use mocked HTTP responses

## Configuration

### Timeout Configuration

```python
# Default timeout is 30 seconds
client = BaseLinkerClient("token", timeout=60)
```

### Custom Session

```python
import requests
from baselinker import BaseLinkerClient

# Use custom session with additional headers
session = requests.Session()
session.headers.update({'User-Agent': 'MyApp/1.0'})

client = BaseLinkerClient("token")
client.session = session
```

## Requirements

- **Python**: 3.7+
- **Dependencies**: requests >= 2.25.0
- **Development**: pytest, pytest-cov, black, flake8

## API Documentation

Full BaseLinker API documentation: https://api.baselinker.com

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Make changes and add tests
4. Run tests (`pytest`)
5. Commit changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Maintain 90%+ test coverage

## Changelog

### Version 0.1.0
- Initial release
- Complete BaseLinker API integration
- Order management
- Product catalog management
- Warehouse operations
- Courier integration
- External storage support
- Order returns
- Comprehensive test suite (94% coverage)

## Support

- **Issues**: [GitHub Issues](https://github.com/your-username/baselinker-api/issues)
- **Documentation**: [API Docs](https://api.baselinker.com)
- **BaseLinker Support**: [BaseLinker Help](https://baselinker.com/help)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This is an unofficial library for BaseLinker API. BaseLinker is a trademark of BaseLinker Sp. z o.o.