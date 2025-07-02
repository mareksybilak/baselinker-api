import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestExternalStorageModuleComprehensive:
    """Comprehensive tests for ExternalStorageModule"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.external_storage = self.client.external_storage

    @patch('baselinker.client.requests.Session.post')
    def test_get_external_storages_list(self, mock_post):
        """Test get_external_storages_list method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "storages": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.external_storage.get_external_storages_list()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getExternalStoragesList'

    @patch('baselinker.client.requests.Session.post')
    def test_get_external_storage_categories(self, mock_post):
        """Test get_external_storage_categories method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "categories": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.external_storage.get_external_storage_categories(storage_id="allegro_123")
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getExternalStorageCategories'

    def test_get_external_storage_categories_validation(self):
        """Test validation for get_external_storage_categories"""
        with pytest.raises(ValueError, match="Missing required parameters: storage_id"):
            self.external_storage.get_external_storage_categories()

    @patch('baselinker.client.requests.Session.post')
    def test_get_external_storage_products_data(self, mock_post):
        """Test get_external_storage_products_data method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "products": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.external_storage.get_external_storage_products_data(
            storage_id="allegro_123",
            products=["PROD-001", "PROD-002"]
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getExternalStorageProductsData'

    def test_get_external_storage_products_data_validation(self):
        """Test validation for get_external_storage_products_data"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.external_storage.get_external_storage_products_data()

    @patch('baselinker.client.requests.Session.post')
    def test_get_external_storage_products_list(self, mock_post):
        """Test get_external_storage_products_list method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "products": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.external_storage.get_external_storage_products_list(
            storage_id="allegro_123",
            filter_category_id="electronics"
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getExternalStorageProductsList'

    def test_get_external_storage_products_list_validation(self):
        """Test validation for get_external_storage_products_list"""
        with pytest.raises(ValueError, match="Missing required parameters: storage_id"):
            self.external_storage.get_external_storage_products_list()

    @patch('baselinker.client.requests.Session.post')
    def test_get_external_storage_products_quantity(self, mock_post):
        """Test get_external_storage_products_quantity method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "products": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.external_storage.get_external_storage_products_quantity(
            storage_id="allegro_123",
            page=1
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getExternalStorageProductsQuantity'

    def test_get_external_storage_products_quantity_validation(self):
        """Test validation for get_external_storage_products_quantity"""
        with pytest.raises(ValueError, match="Missing required parameters: storage_id"):
            self.external_storage.get_external_storage_products_quantity()

    @patch('baselinker.client.requests.Session.post')
    def test_update_external_storage_products_quantity(self, mock_post):
        """Test update_external_storage_products_quantity method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.external_storage.update_external_storage_products_quantity(
            storage_id="allegro_123",
            products=[{"product_id": "PROD-001", "quantity": 10}]
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'updateExternalStorageProductsQuantity'

    def test_update_external_storage_products_quantity_validation(self):
        """Test validation for update_external_storage_products_quantity"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.external_storage.update_external_storage_products_quantity()

    @patch('baselinker.client.requests.Session.post')
    def test_get_external_storage_products_prices(self, mock_post):
        """Test get_external_storage_products_prices method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "products": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.external_storage.get_external_storage_products_prices(
            storage_id="allegro_123",
            page=1
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getExternalStorageProductsPrices'

    def test_get_external_storage_products_prices_validation(self):
        """Test validation for get_external_storage_products_prices"""
        with pytest.raises(ValueError, match="Missing required parameters: storage_id"):
            self.external_storage.get_external_storage_products_prices()

    @patch('baselinker.client.requests.Session.post')
    def test_update_external_storage_products_prices(self, mock_post):
        """Test update_external_storage_products_prices method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.external_storage.update_external_storage_products_prices(
            storage_id="allegro_123",
            products=[{"product_id": "PROD-001", "price": 29.99}]
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'updateExternalStorageProductsPrices'

    def test_update_external_storage_products_prices_validation(self):
        """Test validation for update_external_storage_products_prices"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.external_storage.update_external_storage_products_prices()