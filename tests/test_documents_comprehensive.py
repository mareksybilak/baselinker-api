import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestDocumentsModuleComprehensive:
    """Comprehensive tests for DocumentsModule"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.documents = self.client.documents

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_documents(self, mock_post):
        """Test get_inventory_documents method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "documents": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.documents.get_inventory_documents(
            inventory_id=123,
            date_from=1640995200
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryDocuments'

    def test_get_inventory_documents_validation(self):
        """Test validation for get_inventory_documents"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.documents.get_inventory_documents()

    @patch('baselinker.client.requests.Session.post')
    def test_add_inventory_document(self, mock_post):
        """Test add_inventory_document method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "document_id": 456}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.documents.add_inventory_document(
            inventory_id=123,
            type="receipt",
            series="REC",
            number="001"
        )
        
        assert result["document_id"] == 456
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addInventoryDocument'

    def test_add_inventory_document_validation(self):
        """Test validation for add_inventory_document"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.documents.add_inventory_document()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_document(self, mock_post):
        """Test get_inventory_document method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "document": {}}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.documents.get_inventory_document(document_id=456)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryDocument'

    def test_get_inventory_document_validation(self):
        """Test validation for get_inventory_document"""
        with pytest.raises(ValueError, match="Missing required parameters: document_id"):
            self.documents.get_inventory_document()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_inventory_document(self, mock_post):
        """Test delete_inventory_document method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.documents.delete_inventory_document(document_id=456)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteInventoryDocument'

    def test_delete_inventory_document_validation(self):
        """Test validation for delete_inventory_document"""
        with pytest.raises(ValueError, match="Missing required parameters: document_id"):
            self.documents.delete_inventory_document()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_purchase_orders(self, mock_post):
        """Test get_inventory_purchase_orders method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "orders": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.documents.get_inventory_purchase_orders(
            inventory_id=123,
            date_from=1640995200
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryPurchaseOrders'

    def test_get_inventory_purchase_orders_validation(self):
        """Test validation for get_inventory_purchase_orders"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.documents.get_inventory_purchase_orders()

    @patch('baselinker.client.requests.Session.post')
    def test_add_inventory_purchase_order(self, mock_post):
        """Test add_inventory_purchase_order method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "purchase_order_id": 789}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.documents.add_inventory_purchase_order(
            inventory_id=123,
            supplier_id=456,
            products=[{"product_id": "PROD-001", "quantity": 10}]
        )
        
        assert result["purchase_order_id"] == 789
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addInventoryPurchaseOrder'

    def test_add_inventory_purchase_order_validation(self):
        """Test validation for add_inventory_purchase_order"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.documents.add_inventory_purchase_order()