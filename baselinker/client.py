import json
import requests
from typing import Dict, Any, Optional
from .exceptions import BaseLinkerError, AuthenticationError, RateLimitError, APIError
from .modules import (
    OrdersModule,
    ProductsModule,
    InventoryModule,
    CourierModule,
    ExternalStorageModule,
    ReturnsModule,
    InvoicesModule,
    DocumentsModule,
    DevicesModule
)


class BaseLinkerClient:
    """
    BaseLinker API client for Python integration with modular architecture.
    
    This client provides access to all BaseLinker API functionality through
    specialized modules for different areas of functionality:
    
    - orders: Order management and processing
    - products: Product catalog management
    - inventory: Warehouse and inventory operations
    - courier: Shipping and courier services
    - invoices: Invoice and payment management
    - returns: Order returns processing
    - external_storage: External marketplace integration
    - documents: Warehouse document management
    - devices: Device management and automation
    
    Example:
        client = BaseLinkerClient("your_api_token")
        
        # Get orders using orders module
        orders = client.orders.get_orders()
        
        # Search orders by email
        customer_orders = client.orders.get_orders_by_email(email="customer@example.com")
        
        # Get products from catalog
        products = client.products.get_inventory_products_list(inventory_id=123)
        
        # Create invoice
        invoice = client.invoices.add_invoice(order_id=456)
    """
    
    BASE_URL = "https://api.baselinker.com/connector.php"
    
    def __init__(self, token: str, timeout: int = 30):
        """
        Initialize BaseLinker client
        
        Args:
            token: API token from BaseLinker account
            timeout: Request timeout in seconds
        """
        if not token:
            raise AuthenticationError("API token is required")
        
        self.token = token
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'X-BLToken': token,
            'Content-Type': 'application/x-www-form-urlencoded'
        })
        
        # Initialize modules
        self.orders = OrdersModule(self)
        self.products = ProductsModule(self)
        self.inventory = InventoryModule(self)
        self.courier = CourierModule(self)
        self.external_storage = ExternalStorageModule(self)
        self.returns = ReturnsModule(self)
        self.invoices = InvoicesModule(self)
        self.documents = DocumentsModule(self)
        self.devices = DevicesModule(self)
    
    def _make_request(self, method: str, parameters: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make API request to BaseLinker
        
        Args:
            method: API method name
            parameters: Method parameters
            
        Returns:
            API response data
            
        Raises:
            AuthenticationError: Invalid token
            RateLimitError: Rate limit exceeded
            APIError: API error response
            BaseLinkerError: Other API errors
        """
        if parameters is None:
            parameters = {}
        
        data = {
            'method': method,
            'parameters': json.dumps(parameters)
        }
        
        try:
            response = self.session.post(
                self.BASE_URL,
                data=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            
        except requests.exceptions.Timeout:
            raise BaseLinkerError("Request timeout")
        except requests.exceptions.RequestException as e:
            raise BaseLinkerError(f"Request failed: {str(e)}")
        
        try:
            result = response.json()
        except json.JSONDecodeError:
            raise BaseLinkerError("Invalid JSON response")
        
        if 'error_code' in result:
            error_code = result.get('error_code')
            error_message = result.get('error_message', 'Unknown error')
            
            if error_code == 'ERROR_AUTH_TOKEN':
                raise AuthenticationError(error_message)
            elif error_code == 'ERROR_RATE_LIMIT':
                raise RateLimitError(error_message)
            else:
                raise APIError(error_message, error_code)
        
        return result