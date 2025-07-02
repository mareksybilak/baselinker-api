import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient
from baselinker.exceptions import AuthenticationError, RateLimitError, APIError


class TestBaseLinkerClient:
    
    def test_init_without_token_raises_error(self):
        with pytest.raises(AuthenticationError):
            BaseLinkerClient("")
    
    def test_init_with_token(self):
        client = BaseLinkerClient("test-token")
        assert client.token == "test-token"
        assert client.session.headers['X-BLToken'] == "test-token"
    
    @patch('requests.Session.post')
    def test_successful_request(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "orders": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client._make_request("getOrders", {"date_from": 123456})
        
        assert result == {"status": "SUCCESS", "orders": []}
        mock_post.assert_called_once()
    
    @patch('requests.Session.post')
    def test_authentication_error(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_AUTH_TOKEN",
            "error_message": "Invalid token"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("invalid-token")
        
        with pytest.raises(AuthenticationError):
            client._make_request("getOrders")
    
    @patch('requests.Session.post')
    def test_rate_limit_error(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_RATE_LIMIT",
            "error_message": "Rate limit exceeded"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        
        with pytest.raises(RateLimitError):
            client._make_request("getOrders")
    
    @patch('requests.Session.post')
    def test_api_error(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_UNKNOWN",
            "error_message": "Unknown error"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        
        with pytest.raises(APIError) as exc_info:
            client._make_request("getOrders")
        
        assert exc_info.value.error_code == "ERROR_UNKNOWN"
    
    @patch('requests.Session.post')
    def test_get_orders(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"orders": [{"order_id": 123}]}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.orders.get_orders(date_from=123456)
        
        assert "orders" in result
        expected_data = {
            'method': 'getOrders',
            'parameters': json.dumps({"date_from": 123456})
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_order_management_methods(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        
        # Test order sources
        result = client.orders.get_order_sources()
        assert result == {"status": "SUCCESS"}
        
        # Test set order status
        result = client.orders.set_order_status(order_id=123, status_id=1)
        assert result == {"status": "SUCCESS"}
        
        # Test add order product
        result = client.orders.add_order_product(
            order_id=123, 
            product_id="ABC", 
            name="Test Product",
            price_brutto=29.99,
            tax_rate=23.0,
            quantity=1
        )
        assert result == {"status": "SUCCESS"}
    
    @patch('requests.Session.post')
    def test_inventory_methods(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"products": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        
        # Test get inventory products data
        result = client.products.get_inventory_products_data(inventory_id=123, products=["ABC", "DEF"])
        assert "products" in result
        
        # Test update stock
        result = client.products.update_inventory_products_stock(
            inventory_id=123,
            products=[{"product_id": "ABC", "stock": 10}]
        )
        assert "products" in result
    
    @patch('requests.Session.post')
    def test_courier_methods(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"package_id": 123}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        
        # Test create package manual
        result = client.courier.create_package_manual(
            order_id=123,
            courier_code="DPD",
            package_number="123456789"
        )
        assert result == {"package_id": 123}
        
        # Test get label
        result = client.courier.get_label(package_id=123)
        assert result == {"package_id": 123}
    
    @patch('requests.Session.post')
    def test_external_storage_methods(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"storages": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        
        # Test get external storages
        result = client.external_storage.get_external_storages_list()
        assert "storages" in result
        
        # Test get products data
        result = client.external_storage.get_external_storage_products_data(storage_id="123", products=["ABC", "DEF"])
        assert "storages" in result