import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient
from baselinker.exceptions import AuthenticationError, APIError


class TestOrderManagement:
    
    @patch('requests.Session.post')
    def test_get_order_sources(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "sources": [
                {"id": 1, "name": "Shop"},
                {"id": 2, "name": "Allegro"}
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.orders.get_order_sources()
        
        assert "sources" in result
        assert len(result["sources"]) == 2
        
        expected_data = {
            'method': 'getOrderSources',
            'parameters': json.dumps({})
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_set_order_fields(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        order_data = {
            "order_id": 123,
            "admin_comments": "Updated comment",
            "delivery_price": 15.99
        }
        result = client.orders.set_order_fields(**order_data)
        
        assert result["status"] == "SUCCESS"
        
        expected_data = {
            'method': 'setOrderFields',
            'parameters': json.dumps(order_data)
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_set_order_status(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.orders.set_order_status(order_id=123, status_id=2)
        
        assert result["status"] == "SUCCESS"
        
        expected_data = {
            'method': 'setOrderStatus',
            'parameters': json.dumps({"order_id": 123, "status_id": 2})
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_add_order_product(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "order_product_id": 456}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        product_data = {
            "order_id": 123,
            "product_id": "ABC123",
            "name": "Test Product",
            "quantity": 2,
            "price_brutto": 29.99,
            "tax_rate": 23.0
        }
        result = client.orders.add_order_product(**product_data)
        
        assert result["status"] == "SUCCESS"
        assert result["order_product_id"] == 456
        
        expected_data = {
            'method': 'addOrderProduct',
            'parameters': json.dumps(product_data)
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_set_order_product_fields(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        update_data = {
            "order_id": 123,
            "order_product_id": 456,
            "quantity": 3,
            "price": 24.99
        }
        result = client.orders.set_order_product_fields(**update_data)
        
        assert result["status"] == "SUCCESS"
    
    @patch('requests.Session.post')
    def test_delete_order_product(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.orders.delete_order_product(order_id=123, order_product_id=456)
        
        assert result["status"] == "SUCCESS"
    
    @patch('requests.Session.post')
    def test_get_journal_list(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "journal": [
                {"log_id": 1, "order_id": 123, "changes": "Status changed"},
                {"log_id": 2, "order_id": 124, "changes": "Product added"}
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.orders.get_journal_list(last_log_id=0)
        
        assert "journal" in result
        assert len(result["journal"]) == 2
    
    @patch('requests.Session.post')
    def test_get_order_transaction_data(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "transaction_id": "TXN123",
            "amount": 99.99,
            "currency": "PLN",
            "status": "completed"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.orders.get_order_transaction_data(order_id=123)
        
        assert result["transaction_id"] == "TXN123"
        assert result["amount"] == 99.99
    
    @patch('requests.Session.post')
    def test_get_order_payments_history(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "payments": [
                {"payment_id": 1, "amount": 50.00, "date": "2023-01-01"},
                {"payment_id": 2, "amount": 49.99, "date": "2023-01-02"}
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.invoices.get_order_payments_history(order_id=123)
        
        assert "payments" in result
        assert len(result["payments"]) == 2