import json
import requests
from typing import Dict, Any, Optional
from .exceptions import BaseLinkerError, AuthenticationError, RateLimitError, APIError


class BaseLinkerClient:
    """BaseLinker API client for Python integration"""
    
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
    
    def get_orders(self, **kwargs) -> Dict[str, Any]:
        """
        Download orders from BaseLinker order manager.
        
        Args:
            order_id (int, optional): Specific order identifier
            date_confirmed_from (int, optional): Unix timestamp - confirmed orders from this date
            date_from (int, optional): Unix timestamp - orders created from this date
            date_to (int, optional): Unix timestamp - orders created until this date
            id_from (int, optional): Order ID to start collecting subsequent orders
            id_to (int, optional): Order ID to end collecting orders
            get_unconfirmed_orders (bool, optional): Include unconfirmed orders (default: false)
            include_custom_extra_fields (bool, optional): Download custom field values (default: false)
            status_id (int, optional): Filter by specific order status
            filter_email (str, optional): Filter by customer email (max 50 chars)
            filter_order_source (str, optional): Filter by order source (max 20 chars)
            filter_order_source_id (int, optional): Specific order source identifier
            with_commission (bool, optional): Include commission information (default: false)
            
        Returns:
            Dict containing orders list (max 100 orders per request)
            
        Raises:
            AuthenticationError: Invalid API token
            RateLimitError: Rate limit exceeded
            APIError: API-specific error
        """
        return self._make_request('getOrders', kwargs)
    
    def add_order(self, **kwargs) -> Dict[str, Any]:
        """
        Add new order to BaseLinker order manager.
        
        Required Args:
            order_source_id (int): Order source identifier
            date_add (int): Order creation timestamp (Unix)
            order_status_id (int): Order status
            
        Optional Args:
            currency (str): 3-letter currency code (e.g., "PLN", "EUR", "USD")
            payment_method (str): Payment method name (max 30 chars)
            payment_method_cod (bool): Cash on delivery flag
            payment_done (float): Payment amount received
            delivery_method (str): Shipping method name (max 30 chars)
            delivery_price (float): Gross delivery price
            delivery_fullname (str): Delivery recipient name (max 100 chars)
            delivery_company (str): Delivery company name (max 100 chars)
            delivery_address (str): Delivery street address (max 100 chars)
            delivery_city (str): Delivery city (max 50 chars)
            delivery_postcode (str): Delivery postal code (max 20 chars)
            delivery_country_code (str): Delivery country (2-letter code)
            invoice_fullname (str): Invoice recipient name (max 100 chars)
            invoice_company (str): Invoice company name (max 100 chars)
            invoice_nip (str): Tax identification number (max 20 chars)
            want_invoice (bool): Invoice required flag
            user_comments (str): Customer comments
            admin_comments (str): Admin comments
            email (str): Customer email (max 150 chars)
            phone (str): Customer phone (max 50 chars)
            products (list): Array of order products
            
        Returns:
            Dict with new order_id
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Missing required parameters or other API error
        """
        return self._make_request('addOrder', kwargs)
    
    def get_inventory_products_list(self, **kwargs) -> Dict[str, Any]:
        """
        Get products list from BaseLinker catalog.
        
        Required Args:
            inventory_id (int): Catalog identifier
            
        Optional Args:
            filter_category_id (int): Filter by category
            filter_limit (int): Results limit (max 1000, default 1000)
            filter_offset (int): Results offset for pagination
            filter_sort (str): Sort field (id/name/quantity/price)
            filter_id (str): Filter by product ID (max 30 chars)
            filter_ean (str): Filter by EAN (max 20 chars)
            filter_sku (str): Filter by SKU (max 50 chars)
            filter_name (str): Filter by product name (max 100 chars)
            filter_price_from (float): Minimum price
            filter_price_to (float): Maximum price
            filter_quantity_from (int): Minimum quantity
            filter_quantity_to (int): Maximum quantity
            filter_available (int): Filter by availability (0=all, 1=available, 2=unavailable)
            
        Returns:
            Dict containing products list with basic information
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid inventory_id or other API error
        """
        return self._make_request('getInventoryProductsList', kwargs)
    
    def add_inventory_product(self, **kwargs) -> Dict[str, Any]:
        """
        Add or update product in BaseLinker catalog.
        
        Required Args:
            inventory_id (int): Catalog identifier
            product_id (str): Product identifier (max 30 chars)
            
        Optional Args:
            parent_id (str): Parent product ID for variants (max 30 chars)
            is_bundle (bool): Bundle product flag
            ean (str): EAN code (max 20 chars)
            sku (str): SKU code (max 50 chars)
            tax_rate (float): VAT tax rate (0-100)
            weight (float): Product weight in kg
            width (float): Product width in cm
            height (float): Product height in cm
            length (float): Product length in cm
            star (int): Star rating (0-5)
            manufacturer_id (int): Manufacturer identifier
            category_id (int): Category identifier
            prices (dict): Price groups data with price_netto, price_brutto, etc.
            stock (dict): Warehouse stock levels {"warehouse_id": quantity}
            locations (dict): Warehouse locations {"warehouse_id": "location"}
            text_fields (dict): Multilingual text content (name, description, etc.)
            images (list): Product images with url, title, sort
            links (list): Related links
            
        Returns:
            Dict with product_id of created/updated product
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid parameters or other API error
        """
        return self._make_request('addInventoryProduct', kwargs)
    
    def get_inventory_products_stock(self, **kwargs) -> Dict[str, Any]:
        """
        Get product stock levels from BaseLinker catalog.
        
        Required Args:
            inventory_id (int): Catalog identifier
            products (list): Array of product IDs to check
            
        Returns:
            Dict containing stock levels for each product and warehouse
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid inventory_id or other API error
        """
        return self._make_request('getInventoryProductsStock', kwargs)
    
    def create_package(self, **kwargs) -> Dict[str, Any]:
        """
        Create shipment package in courier system.
        
        Required Args:
            order_id (int): Order identifier
            courier_code (str): Courier code (e.g., "dpd", "ups", "fedex")
            
        Optional Args:
            account_id (int): Courier API account identifier
            fields (dict): Courier-specific form fields
            packages (list): Package details with size, weight, dimensions
            
        Package Fields:
            size (str): Package size (S/M/L/XL)
            weight (float): Package weight in kg
            width (float): Package width in cm
            height (float): Package height in cm
            length (float): Package length in cm
            declared_content (str): Content description
            insurance (bool): Insurance flag
            insurance_value (float): Insurance value
            cod_amount (float): Cash on delivery amount
            delivery_confirmation (bool): Delivery confirmation required
            
        Returns:
            Dict with package_id, package_number, courier_inner_number, tracking_number
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid order_id, courier_code or other API error
        """
        return self._make_request('createPackage', kwargs)
    
    def get_couriers_list(self) -> Dict[str, Any]:
        """
        Get list of available couriers.
        
        Returns:
            Dict containing list of available couriers with their codes, names, services, and supported countries
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: API error
        """
        return self._make_request('getCouriersList')
    
    def get_inventories(self) -> Dict[str, Any]:
        """
        Get list of BaseLinker catalogs.
        
        Returns:
            Dict containing inventories with their IDs, names, descriptions, languages, price groups, and warehouses
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: API error
        """
        return self._make_request('getInventories')
    
    def get_categories(self, **kwargs) -> Dict[str, Any]:
        """
        Get product categories from BaseLinker catalog.
        
        Required Args:
            inventory_id (int): Catalog identifier
            
        Returns:
            Dict containing categories with their IDs, names, parent relationships, and sort order
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid inventory_id or other API error
        """
        return self._make_request('getInventoryCategories', kwargs)
    
    # Order Management Methods
    def get_order_sources(self) -> Dict[str, Any]:
        """
        Get list of order sources.
        
        Returns:
            Dict containing available order sources with their IDs, names, and types
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: API error
        """
        return self._make_request('getOrderSources')
    
    def set_order_fields(self, **kwargs) -> Dict[str, Any]:
        """
        Edit specific fields of an existing order.
        
        Required Args:
            order_id (int): Order identifier
            
        Optional Args:
            admin_comments (str): Admin comments
            user_comments (str): Customer comments
            payment_method (str): Payment method (max 30 chars)
            payment_method_cod (bool): Cash on delivery flag
            payment_done (float): Payment amount received
            delivery_method (str): Delivery method (max 30 chars)
            delivery_price (float): Delivery price
            delivery_fullname (str): Delivery recipient name (max 100 chars)
            delivery_company (str): Delivery company (max 100 chars)
            delivery_address (str): Delivery address (max 100 chars)
            delivery_city (str): Delivery city (max 50 chars)
            delivery_postcode (str): Delivery postcode (max 20 chars)
            delivery_country_code (str): Delivery country (2-letter code)
            phone (str): Phone number (max 50 chars)
            email (str): Email address (max 150 chars)
            pick_state (int): Pick state
            pack_state (int): Pack state
            
        Returns:
            Dict with operation status
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid order_id or other API error
        """
        return self._make_request('setOrderFields', kwargs)
    
    def set_order_status(self, **kwargs) -> Dict[str, Any]:
        """
        Change order status.
        
        Required Args:
            order_id (int): Order identifier
            status_id (int): New status identifier
            
        Returns:
            Dict with operation status
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid order_id or status_id
        """
        return self._make_request('setOrderStatus', kwargs)
    
    def add_order_product(self, **kwargs) -> Dict[str, Any]:
        """
        Add product to existing order.
        
        Required Args:
            order_id (int): Order identifier
            product_id (str): Product identifier (max 30 chars)
            name (str): Product name (max 200 chars)
            price_brutto (float): Gross price
            tax_rate (float): Tax rate (0-100)
            quantity (int): Quantity
            
        Optional Args:
            storage (str): Storage type (bl/shop/warehouse, max 20 chars)
            storage_id (int): Storage identifier
            variant_id (int): Product variant ID
            attributes (str): Product attributes (max 50 chars)
            sku (str): SKU code (max 50 chars)
            ean (str): EAN code (max 20 chars)
            location (str): Storage location (max 10 chars)
            warehouse_id (int): Warehouse identifier
            auction_id (str): Auction identifier (max 20 chars)
            weight (float): Product weight
            
        Returns:
            Dict with order_product_id of added product
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid parameters or other API error
        """
        return self._make_request('addOrderProduct', kwargs)
    
    def set_order_product_fields(self, **kwargs) -> Dict[str, Any]:
        """Update order product fields"""
        return self._make_request('setOrderProductFields', kwargs)
    
    def delete_order_product(self, **kwargs) -> Dict[str, Any]:
        """Delete product from order"""
        return self._make_request('deleteOrderProduct', kwargs)
    
    def get_journal_list(self, **kwargs) -> Dict[str, Any]:
        """Get journal entries list"""
        return self._make_request('getJournalList', kwargs)
    
    def get_order_transaction_data(self, **kwargs) -> Dict[str, Any]:
        """Get order transaction data"""
        return self._make_request('getOrderTransactionData', kwargs)
    
    def get_order_payments_history(self, **kwargs) -> Dict[str, Any]:
        """Get order payments history"""
        return self._make_request('getOrderPaymentsHistory', kwargs)
    
    # Product Catalog Methods
    def get_inventory_products_data(self, **kwargs) -> Dict[str, Any]:
        """Get detailed inventory products data"""
        return self._make_request('getInventoryProductsData', kwargs)
    
    def delete_inventory_product(self, **kwargs) -> Dict[str, Any]:
        """Delete product from inventory"""
        return self._make_request('deleteInventoryProduct', kwargs)
    
    def update_inventory_products_stock(self, **kwargs) -> Dict[str, Any]:
        """
        Update product stock levels in BaseLinker catalog.
        
        Required Args:
            inventory_id (int): Catalog identifier
            products (list): Array of stock updates with product_id, variant_id, and stock dict
            
        Product Structure:
            {
                "product_id": "PROD-001",
                "variant_id": 0,
                "stock": {
                    "bl_123": 100,  # warehouse_id: quantity
                    "shop_456": 50
                }
            }
            
        Limitations:
            Maximum 1000 products per request
            
        Returns:
            Dict with operation status and warnings if any
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid parameters or other API error
        """
        return self._make_request('updateInventoryProductsStock', kwargs)
    
    def update_inventory_products_prices(self, **kwargs) -> Dict[str, Any]:
        """Update inventory products prices"""
        return self._make_request('updateInventoryProductsPrices', kwargs)
    
    def get_inventory_categories(self, **kwargs) -> Dict[str, Any]:
        """Get inventory categories"""
        return self._make_request('getInventoryCategories', kwargs)
    
    def add_inventory_category(self, **kwargs) -> Dict[str, Any]:
        """Add new inventory category"""
        return self._make_request('addInventoryCategory', kwargs)
    
    def delete_inventory_category(self, **kwargs) -> Dict[str, Any]:
        """Delete inventory category"""
        return self._make_request('deleteInventoryCategory', kwargs)
    
    def add_inventory(self, **kwargs) -> Dict[str, Any]:
        """Add new inventory"""
        return self._make_request('addInventory', kwargs)
    
    def delete_inventory(self, **kwargs) -> Dict[str, Any]:
        """Delete inventory"""
        return self._make_request('deleteInventory', kwargs)
    
    # Warehouse Methods
    def get_inventory_warehouses(self, **kwargs) -> Dict[str, Any]:
        """Get inventory warehouses"""
        return self._make_request('getInventoryWarehouses', kwargs)
    
    def add_inventory_warehouse(self, **kwargs) -> Dict[str, Any]:
        """Add new inventory warehouse"""
        return self._make_request('addInventoryWarehouse', kwargs)
    
    def delete_inventory_warehouse(self, **kwargs) -> Dict[str, Any]:
        """Delete inventory warehouse"""
        return self._make_request('deleteInventoryWarehouse', kwargs)
    
    def get_inventory_price_groups(self, **kwargs) -> Dict[str, Any]:
        """Get inventory price groups"""
        return self._make_request('getInventoryPriceGroups', kwargs)
    
    def add_inventory_price_group(self, **kwargs) -> Dict[str, Any]:
        """Add new inventory price group"""
        return self._make_request('addInventoryPriceGroup', kwargs)
    
    def delete_inventory_price_group(self, **kwargs) -> Dict[str, Any]:
        """Delete inventory price group"""
        return self._make_request('deleteInventoryPriceGroup', kwargs)
    
    # Courier & Shipping Methods
    def create_package_manual(self, **kwargs) -> Dict[str, Any]:
        """Create courier package manually"""
        return self._make_request('createPackageManual', kwargs)
    
    def get_label(self, **kwargs) -> Dict[str, Any]:
        """Get shipping label"""
        return self._make_request('getLabel', kwargs)
    
    def get_order_packages(self, **kwargs) -> Dict[str, Any]:
        """Get order packages"""
        return self._make_request('getOrderPackages', kwargs)
    
    def request_parcel_pickup(self, **kwargs) -> Dict[str, Any]:
        """Request parcel pickup"""
        return self._make_request('requestParcelPickup', kwargs)
    
    # External Storage Methods
    def get_external_storages_list(self) -> Dict[str, Any]:
        """
        Get list of external storage connections.
        
        Returns:
            Dict containing external storages with their IDs, names, types, status, and URLs
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: API error
        """
        return self._make_request('getExternalStoragesList')
    
    def get_external_storage_products_data(self, **kwargs) -> Dict[str, Any]:
        """Get external storage products data"""
        return self._make_request('getExternalStorageProductsData', kwargs)
    
    def get_external_storage_products_quantity(self, **kwargs) -> Dict[str, Any]:
        """Get external storage products quantity"""
        return self._make_request('getExternalStorageProductsQuantity', kwargs)
    
    def update_external_storage_products_quantity(self, **kwargs) -> Dict[str, Any]:
        """
        Update product stock quantities in external storage.
        
        Required Args:
            storage_id (str): External storage identifier (max 30 chars)
            products (list): Array of products with stock updates
            
        Product Structure:
            {
                "product_id": "EXT123",
                "variants": [
                    {
                        "variant_id": "VAR1",
                        "stock": 20
                    }
                ]
            }
            
        Limitations:
            Maximum 1000 products per request
            
        Returns:
            Dict with operation status, updated_products count, and warnings if any
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid storage_id or other API error
        """
        return self._make_request('updateExternalStorageProductsQuantity', kwargs)
    
    # Order Returns Methods
    def add_order_return(self, **kwargs) -> Dict[str, Any]:
        """
        Add new order return.
        
        Required Args:
            order_id (int): Order identifier
            return_status (int): Return status identifier
            products (list): Array of returned products with order_product_id, quantity, reason
            
        Optional Args:
            return_reason (str): Return reason (max 100 chars)
            admin_comments (str): Admin comments
            return_address (dict): Return address details
            refund_amount (float): Refund amount
            refund_method (str): Refund method (max 50 chars)
            
        Product Structure:
            {
                "order_product_id": 456,
                "quantity": 1,
                "reason": "Damaged item",
                "refund_amount": 29.99
            }
            
        Returns:
            Dict with return_id of created return
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: Invalid parameters or other API error
        """
        return self._make_request('addOrderReturn', kwargs)
    
    def get_order_returns(self, **kwargs) -> Dict[str, Any]:
        """
        Get order returns from specific date.
        
        Optional Args:
            date_confirmed_from (int): Unix timestamp - confirmed returns from this date
            date_from (int): Unix timestamp - returns created from this date
            date_to (int): Unix timestamp - returns created until this date
            return_status (int): Filter by return status
            order_id (int): Filter by specific order
            get_unconfirmed_returns (bool): Include unconfirmed returns
            
        Limitations:
            Maximum 100 returns per request
            
        Returns:
            Dict containing returns list with detailed information
            
        Raises:
            AuthenticationError: Invalid API token
            APIError: API error
        """
        return self._make_request('getOrderReturns', kwargs)
    
    def set_order_return_fields(self, **kwargs) -> Dict[str, Any]:
        """Update order return fields"""
        return self._make_request('setOrderReturnFields', kwargs)
    
    def set_order_return_status(self, **kwargs) -> Dict[str, Any]:
        """Update order return status"""
        return self._make_request('setOrderReturnStatus', kwargs)