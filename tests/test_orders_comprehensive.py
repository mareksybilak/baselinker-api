import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient
from baselinker.exceptions import BaseLinkerError


class TestOrdersModuleComprehensive:
    """Comprehensive tests for OrdersModule"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.orders = self.client.orders

    @patch('baselinker.client.requests.Session.post')
    def test_get_orders_minimal(self, mock_post):
        """Test get_orders with minimal parameters"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "orders": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_orders(date_from=1640995200)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrders'

    @patch('baselinker.client.requests.Session.post')
    def test_get_orders_full_parameters(self, mock_post):
        """Test get_orders with all parameters"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "orders": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_orders(
            date_from=1640995200,
            date_to=1641081600, 
            id_from=100,
            id_to=200,
            filter_order_source_id=1,
            filter_status=2,
            get_unconfirmed_orders=True,
            include_custom_extra_fields=True
        )
        
        assert result["status"] == "SUCCESS"
        params = json.loads(mock_post.call_args[1]['data']['parameters'])
        assert params['date_from'] == 1640995200
        assert params['get_unconfirmed_orders'] == True

    @patch('baselinker.client.requests.Session.post')
    def test_get_orders_by_email(self, mock_post):
        """Test get_orders_by_email method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "orders": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_orders_by_email(email="test@example.com")
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrdersByEmail'

    def test_get_orders_by_email_validation(self):
        """Test validation for get_orders_by_email"""
        with pytest.raises(ValueError, match="Missing required parameters: email"):
            self.orders.get_orders_by_email()

    @patch('baselinker.client.requests.Session.post')
    def test_get_orders_by_phone(self, mock_post):
        """Test get_orders_by_phone method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "orders": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_orders_by_phone(phone="+48123456789")
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrdersByPhone'

    def test_get_orders_by_phone_validation(self):
        """Test validation for get_orders_by_phone"""
        with pytest.raises(ValueError, match="Missing required parameters: phone"):
            self.orders.get_orders_by_phone()

    @patch('baselinker.client.requests.Session.post')
    def test_add_order(self, mock_post):
        """Test add_order method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "order_id": 12345}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.add_order(
            order_source_id=1,
            date_add=1640995200,
            order_status_id=1,
            user_comments="Test order",
            phone="+48123456789",
            email="test@example.com"
        )
        
        assert result["order_id"] == 12345
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addOrder'

    def test_add_order_validation(self):
        """Test validation for add_order"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.orders.add_order()

        with pytest.raises(ValueError, match="Missing required parameters"):
            self.orders.add_order(order_source_id=1)

    @patch('baselinker.client.requests.Session.post')
    def test_get_order_sources(self, mock_post):
        """Test get_order_sources method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "sources": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_order_sources()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderSources'

    @patch('baselinker.client.requests.Session.post')
    def test_get_order_extra_fields(self, mock_post):
        """Test get_order_extra_fields method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "fields": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_order_extra_fields()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderExtraFields'

    @patch('baselinker.client.requests.Session.post')
    def test_get_order_status_list(self, mock_post):
        """Test get_order_status_list method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "statuses": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_order_status_list()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderStatusList'

    @patch('baselinker.client.requests.Session.post')
    def test_set_order_fields(self, mock_post):
        """Test set_order_fields method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.set_order_fields(
            order_id=12345,
            admin_comments="Updated via API"
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'setOrderFields'

    def test_set_order_fields_validation(self):
        """Test validation for set_order_fields"""
        with pytest.raises(ValueError, match="Missing required parameters: order_id"):
            self.orders.set_order_fields()

    @patch('baselinker.client.requests.Session.post')
    def test_set_order_status(self, mock_post):
        """Test set_order_status method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.set_order_status(order_id=12345, status_id=2)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'setOrderStatus'

    def test_set_order_status_validation(self):
        """Test validation for set_order_status"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.orders.set_order_status()

    @patch('baselinker.client.requests.Session.post')
    def test_add_order_product(self, mock_post):
        """Test add_order_product method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "order_product_id": 456}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.add_order_product(
            order_id=12345,
            product_id="PROD-001",
            name="Test Product",
            price_brutto=29.99,
            tax_rate=23.0,
            quantity=1
        )
        
        assert result["order_product_id"] == 456
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addOrderProduct'

    def test_add_order_product_validation(self):
        """Test validation for add_order_product"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.orders.add_order_product()

    @patch('baselinker.client.requests.Session.post')
    def test_set_order_product_fields(self, mock_post):
        """Test set_order_product_fields method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.set_order_product_fields(
            order_id=12345,
            order_product_id=456,
            name="Updated Product Name"
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'setOrderProductFields'

    def test_set_order_product_fields_validation(self):
        """Test validation for set_order_product_fields"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.orders.set_order_product_fields()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_order_product(self, mock_post):
        """Test delete_order_product method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.delete_order_product(
            order_id=12345,
            order_product_id=456
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteOrderProduct'

    def test_delete_order_product_validation(self):
        """Test validation for delete_order_product"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.orders.delete_order_product()

    @patch('baselinker.client.requests.Session.post')
    def test_get_journal_list(self, mock_post):
        """Test get_journal_list method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "journal": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_journal_list(
            last_log_id=0,
            logs_types=[1, 2, 3]
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getJournalList'

    @patch('baselinker.client.requests.Session.post')  
    def test_get_order_transaction_data(self, mock_post):
        """Test get_order_transaction_data method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "transaction": {}}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_order_transaction_data(order_id=12345)
        
        assert result["status"] == "SUCCESS" 
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderTransactionData'

    def test_get_order_transaction_data_validation(self):
        """Test validation for get_order_transaction_data"""
        with pytest.raises(ValueError, match="Missing required parameters: order_id"):
            self.orders.get_order_transaction_data()

    @patch('baselinker.client.requests.Session.post')
    def test_get_order_payments_history(self, mock_post):
        """Test get_order_payments_history method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "payments": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_order_payments_history(order_id=12345)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderPaymentsHistory'

    def test_get_order_payments_history_validation(self):
        """Test validation for get_order_payments_history"""
        with pytest.raises(ValueError, match="Missing required parameters: order_id"):
            self.orders.get_order_payments_history()