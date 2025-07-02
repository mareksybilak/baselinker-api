import pytest
import json
import os
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient
from baselinker.exceptions import AuthenticationError, RateLimitError, APIError


class TestIntegration:
    """Integration tests for BaseLinker API client"""
    
    def test_client_initialization_integration(self):
        """Test client initialization with different configurations"""
        # Test with token
        client = BaseLinkerClient("test-token")
        assert client.token == "test-token"
        assert client.timeout == 30
        
        # Test with custom timeout
        client_custom = BaseLinkerClient("test-token", timeout=60)
        assert client_custom.timeout == 60
        
        # Test without token should raise error
        with pytest.raises(AuthenticationError):
            BaseLinkerClient("")
    
    @patch('requests.Session.post')
    def test_complete_order_workflow(self, mock_post):
        """Test complete order management workflow"""
        client = BaseLinkerClient("test-token")
        
        # Mock responses for different API calls
        responses = [
            # Add order
            {"status": "SUCCESS", "order_id": 12345},
            # Add product to order
            {"status": "SUCCESS", "order_product_id": 67890},
            # Update order status
            {"status": "SUCCESS"},
            # Get order details
            {"orders": [{"order_id": 12345, "status_id": 2}]},
            # Create package
            {"status": "SUCCESS", "package_id": 111},
            # Get label
            {"status": "SUCCESS", "label": "base64_label_data"}
        ]
        
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Execute workflow
        for i, response in enumerate(responses):
            mock_response.json.return_value = response
            
            if i == 0:
                # Add order
                result = client.orders.add_order(
                    order_source_id=1,
                    date_add=1640995200,
                    order_status_id=1,
                    delivery_price=15.99,
                    user_comments="Test order"
                )
                assert result["order_id"] == 12345
                
            elif i == 1:
                # Add product to order
                result = client.orders.add_order_product(
                    order_id=12345,
                    product_id="TEST123",
                    name="Test Product",
                    quantity=2,
                    price_brutto=29.99,
                    tax_rate=23.0
                )
                assert result["order_product_id"] == 67890
                
            elif i == 2:
                # Update order status
                result = client.orders.set_order_status(order_id=12345, status_id=2)
                assert result["status"] == "SUCCESS"
                
            elif i == 3:
                # Get order details
                result = client.orders.get_orders(order_id=12345)
                assert len(result["orders"]) == 1
                assert result["orders"][0]["status_id"] == 2
                
            elif i == 4:
                # Create package
                result = client.courier.create_package(
                    order_id=12345,
                    courier_code="DPD"
                )
                assert result["package_id"] == 111
                
            elif i == 5:
                # Get shipping label
                result = client.courier.get_label(package_id=111)
                assert "label" in result
    
    @patch('requests.Session.post')
    def test_complete_inventory_workflow(self, mock_post):
        """Test complete inventory management workflow"""
        client = BaseLinkerClient("test-token")
        
        responses = [
            # Get inventories
            {"inventories": [{"inventory_id": 123, "name": "Main"}]},
            # Add product
            {"status": "SUCCESS", "product_id": "NEW123"},
            # Update stock
            {"status": "SUCCESS", "warnings": []},
            # Update prices
            {"status": "SUCCESS", "warnings": []},
            # Get product data
            {"products": [{"product_id": "NEW123", "stock": 50}]}
        ]
        
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        for i, response in enumerate(responses):
            mock_response.json.return_value = response
            
            if i == 0:
                result = client.products.get_inventories()
                assert len(result["inventories"]) == 1
                
            elif i == 1:
                result = client.products.add_inventory_product(
                    inventory_id=123,
                    product_id="NEW123",
                    name="New Product",
                    price_netto=25.00
                )
                assert result["product_id"] == "NEW123"
                
            elif i == 2:
                result = client.products.update_inventory_products_stock(
                    inventory_id=123,
                    products=[{"product_id": "NEW123", "stock": 50}]
                )
                assert result["status"] == "SUCCESS"
                
            elif i == 3:
                result = client.products.update_inventory_products_prices(
                    inventory_id=123,
                    products=[{"product_id": "NEW123", "price_netto": 30.00}]
                )
                assert result["status"] == "SUCCESS"
                
            elif i == 4:
                result = client.products.get_inventory_products_data(
                    inventory_id=123,
                    products=["NEW123"]
                )
                assert result["products"][0]["stock"] == 50
    
    @patch('requests.Session.post')
    def test_error_handling_integration(self, mock_post):
        """Test error handling across different scenarios"""
        client = BaseLinkerClient("test-token")
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test authentication error
        mock_response.json.return_value = {
            "error_code": "ERROR_AUTH_TOKEN",
            "error_message": "Invalid token"
        }
        
        with pytest.raises(AuthenticationError):
            client.orders.get_orders()
        
        # Test rate limit error
        mock_response.json.return_value = {
            "error_code": "ERROR_RATE_LIMIT",
            "error_message": "Rate limit exceeded"
        }
        
        with pytest.raises(RateLimitError):
            client.products.get_inventories()
        
        # Test generic API error
        mock_response.json.return_value = {
            "error_code": "ERROR_UNKNOWN",
            "error_message": "Unknown error occurred"
        }
        
        with pytest.raises(APIError) as exc_info:
            client.orders.add_order(
                order_source_id=1,
                date_add=1640995200,
                order_status_id=1
            )
        
        assert exc_info.value.error_code == "ERROR_UNKNOWN"
    
    @patch('requests.Session.post')
    def test_data_consistency_integration(self, mock_post):
        """Test data consistency across API calls"""
        client = BaseLinkerClient("test-token")
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test that parameters are properly JSON encoded
        test_params = {
            "inventory_id": 123,
            "products": [
                {"product_id": "ABC", "stock": 10},
                {"product_id": "DEF", "stock": 20}
            ],
            "special_chars": "Test ąćę żółć",
            "unicode": "测试数据"
        }
        
        mock_response.json.return_value = {"status": "SUCCESS"}
        
        client.products.update_inventory_products_stock(**test_params)
        
        # Verify the call was made with properly encoded parameters
        call_args = mock_post.call_args
        sent_data = call_args[1]['data']
        
        assert sent_data['method'] == 'updateInventoryProductsStock'
        
        # Verify JSON can be decoded
        parameters = json.loads(sent_data['parameters'])
        assert parameters['inventory_id'] == 123
        assert len(parameters['products']) == 2
        assert parameters['special_chars'] == "Test ąćę żółć"
        assert parameters['unicode'] == "测试数据"
    
    def test_client_session_persistence(self):
        """Test that client maintains session properly"""
        client = BaseLinkerClient("test-token-123")
        
        # Check that session headers are set correctly
        assert client.session.headers['X-BLToken'] == "test-token-123"
        assert 'Content-Type' in client.session.headers
        
        # Test that session is reused
        assert client.session is not None
        session_id = id(client.session)
        
        # Make sure same session is used
        assert id(client.session) == session_id
    
    @patch.dict(os.environ, {'BASELINKER_TOKEN': 'env-token-123'})
    def test_environment_integration(self):
        """Test integration with environment variables"""
        # This would be used in real integration scenarios
        token_from_env = os.environ.get('BASELINKER_TOKEN')
        assert token_from_env == 'env-token-123'
        
        client = BaseLinkerClient(token_from_env)
        assert client.token == 'env-token-123'
    
    @patch('requests.Session.post')
    def test_timeout_configuration(self, mock_post):
        """Test timeout configuration across different operations"""
        import requests
        
        # Test with custom timeout
        client = BaseLinkerClient("test-token", timeout=45)
        
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client.orders.get_orders()
        
        # Verify timeout was passed to request
        call_args = mock_post.call_args
        assert call_args[1]['timeout'] == 45
        
        # Test timeout exception handling
        mock_post.side_effect = requests.exceptions.Timeout("Request timeout")
        
        with pytest.raises(Exception) as exc_info:
            client.orders.get_orders()
        
        assert "timeout" in str(exc_info.value).lower()