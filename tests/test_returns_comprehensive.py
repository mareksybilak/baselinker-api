import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestReturnsModuleComprehensive:
    """Comprehensive tests for ReturnsModule"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.returns = self.client.returns

    @patch('baselinker.client.requests.Session.post')
    def test_get_order_returns(self, mock_post):
        """Test get_order_returns method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "returns": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.returns.get_order_returns(
            order_id=12345,
            limit=10,
            offset=0
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderReturns'

    @patch('baselinker.client.requests.Session.post')
    def test_add_order_return(self, mock_post):
        """Test add_order_return method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "return_id": 123}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.returns.add_order_return(
            order_id=12345,
            reason="damaged",
            comment="Product arrived damaged"
        )
        
        assert result["return_id"] == 123
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addOrderReturn'

    def test_add_order_return_validation(self):
        """Test validation for add_order_return"""
        with pytest.raises(ValueError, match="Missing required parameters: order_id"):
            self.returns.add_order_return()

    @patch('baselinker.client.requests.Session.post')
    def test_set_order_return_fields(self, mock_post):
        """Test set_order_return_fields method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.returns.set_order_return_fields(
            return_id=123,
            comment="Updated comment"
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'setOrderReturnFields'

    def test_set_order_return_fields_validation(self):
        """Test validation for set_order_return_fields"""
        with pytest.raises(ValueError, match="Missing required parameters: return_id"):
            self.returns.set_order_return_fields()

    @patch('baselinker.client.requests.Session.post')
    def test_set_order_return_status(self, mock_post):
        """Test set_order_return_status method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.returns.set_order_return_status(
            return_id=123,
            status_id=2
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'setOrderReturnStatus'

    def test_set_order_return_status_validation(self):
        """Test validation for set_order_return_status"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.returns.set_order_return_status()

    @patch('baselinker.client.requests.Session.post')
    def test_get_order_return_status_list(self, mock_post):
        """Test get_order_return_status_list method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "statuses": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.returns.get_order_return_status_list()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderReturnStatusList'

    @patch('baselinker.client.requests.Session.post')
    def test_get_order_return_reasons(self, mock_post):
        """Test get_order_return_reasons method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "reasons": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.returns.get_order_return_reasons()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderReturnReasons'

    @patch('baselinker.client.requests.Session.post')
    def test_delete_order_return(self, mock_post):
        """Test delete_order_return method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.returns.delete_order_return(return_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteOrderReturn'

    def test_delete_order_return_validation(self):
        """Test validation for delete_order_return"""
        with pytest.raises(ValueError, match="Missing required parameters: return_id"):
            self.returns.delete_order_return()

    @patch('baselinker.client.requests.Session.post')
    def test_get_order_return_products(self, mock_post):
        """Test get_order_return_products method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "products": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.returns.get_order_return_products(return_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderReturnProducts'

    def test_get_order_return_products_validation(self):
        """Test validation for get_order_return_products"""
        with pytest.raises(ValueError, match="Missing required parameters: return_id"):
            self.returns.get_order_return_products()

    @patch('baselinker.client.requests.Session.post')
    def test_add_order_return_product(self, mock_post):
        """Test add_order_return_product method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "return_product_id": 456}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.returns.add_order_return_product(
            return_id=123,
            order_product_id=789,
            quantity=1
        )
        
        assert result["return_product_id"] == 456
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addOrderReturnProduct'

    def test_add_order_return_product_validation(self):
        """Test validation for add_order_return_product"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.returns.add_order_return_product()