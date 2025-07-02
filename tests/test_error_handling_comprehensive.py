import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient
from baselinker.exceptions import (
    BaseLinkerError, 
    AuthenticationError, 
    RateLimitError, 
    APIError
)


class TestErrorHandlingComprehensive:
    """Comprehensive tests for error handling across all modules"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")

    @patch('baselinker.client.requests.Session.post')
    def test_authentication_error_handling(self, mock_post):
        """Test authentication error handling"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_AUTH_TOKEN",
            "error_message": "Invalid token"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        with pytest.raises(AuthenticationError, match="Invalid token"):
            self.client.orders.get_orders(date_from=1640995200)

    @patch('baselinker.client.requests.Session.post')
    def test_rate_limit_error_handling(self, mock_post):
        """Test rate limit error handling"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_RATE_LIMIT",
            "error_message": "Rate limit exceeded"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        with pytest.raises(RateLimitError, match="Rate limit exceeded"):
            self.client.products.get_inventories()

    @patch('baselinker.client.requests.Session.post')
    def test_api_error_handling(self, mock_post):
        """Test generic API error handling"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_UNKNOWN",
            "error_message": "Unknown error occurred"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        with pytest.raises(APIError) as exc_info:
            self.client.courier.get_couriers_list()
        
        assert exc_info.value.error_code == "ERROR_UNKNOWN"
        assert "Unknown error occurred" in str(exc_info.value)

    @patch('baselinker.client.requests.Session.post')
    def test_network_error_handling(self, mock_post):
        """Test network error handling"""
        import requests
        mock_post.side_effect = requests.ConnectionError("Network error")
        
        with pytest.raises(BaseLinkerError, match="Network error"):
            self.client.orders.get_orders(date_from=1640995200)

    @patch('baselinker.client.requests.Session.post')
    def test_timeout_error_handling(self, mock_post):
        """Test timeout error handling"""
        import requests
        mock_post.side_effect = requests.Timeout("Request timeout")
        
        with pytest.raises(BaseLinkerError, match="Request timeout"):
            self.client.products.get_inventories()

    @patch('baselinker.client.requests.Session.post')
    def test_http_error_handling(self, mock_post):
        """Test HTTP error handling"""
        import requests
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("500 Server Error")
        mock_post.return_value = mock_response
        
        with pytest.raises(BaseLinkerError, match="500 Server Error"):
            self.client.courier.get_couriers_list()

    @patch('baselinker.client.requests.Session.post')
    def test_invalid_json_response(self, mock_post):
        """Test handling of invalid JSON response"""
        mock_response = Mock()
        mock_response.json.side_effect = json.JSONDecodeError("Invalid JSON", "", 0)
        mock_response.raise_for_status.return_value = None
        mock_response.text = "Invalid response"
        mock_post.return_value = mock_response
        
        with pytest.raises(BaseLinkerError, match="Invalid JSON response"):
            self.client.orders.get_orders(date_from=1640995200)

    @patch('baselinker.client.requests.Session.post')
    def test_specific_api_errors(self, mock_post):
        """Test specific API error codes"""
        error_scenarios = [
            ("ERROR_INVENTORY_NOT_FOUND", "Inventory not found"),
            ("ERROR_ORDER_NOT_FOUND", "Order not found"),
            ("ERROR_PRODUCT_NOT_FOUND", "Product not found"),
            ("ERROR_INSUFFICIENT_PERMISSIONS", "Insufficient permissions"),
            ("ERROR_INVALID_PARAMETERS", "Invalid parameters")
        ]
        
        for error_code, error_message in error_scenarios:
            mock_response = Mock()
            mock_response.json.return_value = {
                "error_code": error_code,
                "error_message": error_message
            }
            mock_response.raise_for_status.return_value = None
            mock_post.return_value = mock_response
            
            with pytest.raises(APIError) as exc_info:
                self.client.orders.get_orders(date_from=1640995200)
            
            assert exc_info.value.error_code == error_code
            assert error_message in str(exc_info.value)

    def test_validation_errors_orders_module(self):
        """Test validation errors in orders module"""
        # Test missing required parameters
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.orders.add_order()
        
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.orders.get_orders_by_email()
        
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.orders.set_order_status()

    def test_validation_errors_products_module(self):
        """Test validation errors in products module"""
        # Test missing required parameters
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.products.add_inventory_product()
        
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.products.get_inventory_products_data()
        
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.products.update_inventory_products_stock()

    def test_validation_errors_courier_module(self):
        """Test validation errors in courier module"""
        # Test missing required parameters
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.courier.create_package()
        
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.courier.get_courier_services()
        
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.courier.get_label()

    def test_validation_errors_inventory_module(self):
        """Test validation errors in inventory module"""
        # Test missing required parameters
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.inventory.add_inventory_warehouse()
        
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.inventory.add_inventory_price_group()
        
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.inventory.get_inventory_warehouses()

    def test_client_initialization_errors(self):
        """Test client initialization errors"""
        # Test empty token
        with pytest.raises(AuthenticationError, match="API token is required"):
            BaseLinkerClient("")
        
        # Test None token
        with pytest.raises(AuthenticationError, match="API token is required"):
            BaseLinkerClient(None)

    @patch('baselinker.client.requests.Session.post')
    def test_error_message_preservation(self, mock_post):
        """Test that error messages are properly preserved"""
        custom_error_message = "Custom error message with details"
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_CUSTOM",
            "error_message": custom_error_message
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        with pytest.raises(APIError, match=custom_error_message) as exc_info:
            self.client.orders.get_orders(date_from=1640995200)
        
        # Verify error details are preserved
        assert exc_info.value.error_code == "ERROR_CUSTOM"
        assert custom_error_message in str(exc_info.value)

    @patch('baselinker.client.requests.Session.post')
    def test_error_handling_in_all_modules(self, mock_post):
        """Test error handling across all modules"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_TEST",
            "error_message": "Test error"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        modules_and_methods = [
            (self.client.orders, "get_orders", {"date_from": 1640995200}),
            (self.client.products, "get_inventories", {}),
            (self.client.inventory, "get_inventory_warehouses", {"inventory_id": 123}),
            (self.client.courier, "get_couriers_list", {}),
            (self.client.invoices, "get_invoices", {}),
            (self.client.returns, "get_order_returns", {}),
            (self.client.external_storage, "get_external_storages_list", {}),
            (self.client.documents, "get_inventory_documents", {"inventory_id": 123}),
            (self.client.devices, "get_connect_integrations", {})
        ]
        
        for module, method_name, params in modules_and_methods:
            method = getattr(module, method_name)
            with pytest.raises(APIError, match="Test error"):
                method(**params)

    def test_parameter_type_validation(self):
        """Test parameter type validation"""
        # Test invalid parameter types
        with pytest.raises(ValueError):
            # inventory_id should be int, not string
            self.client.inventory.get_inventory_warehouses(inventory_id="invalid")
        
        with pytest.raises(ValueError):
            # date_from should be int, not string
            self.client.orders.get_orders(date_from="invalid")