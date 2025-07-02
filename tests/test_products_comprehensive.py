import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient
from baselinker.exceptions import BaseLinkerError


class TestProductsModuleComprehensive:
    """Comprehensive tests for ProductsModule"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.products = self.client.products

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventories(self, mock_post):
        """Test get_inventories method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "inventories": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventories()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventories'

    @patch('baselinker.client.requests.Session.post')
    def test_add_inventory(self, mock_post):
        """Test add_inventory method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "inventory_id": 123}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.add_inventory(
            name="Test Inventory",
            description="Test Description",
            languages=["en", "pl"]
        )
        
        assert result["inventory_id"] == 123
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addInventory'

    def test_add_inventory_validation(self):
        """Test validation for add_inventory"""
        with pytest.raises(ValueError, match="Missing required parameters: name"):
            self.products.add_inventory()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_inventory(self, mock_post):
        """Test delete_inventory method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.delete_inventory(inventory_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteInventory'

    def test_delete_inventory_validation(self):
        """Test validation for delete_inventory"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.delete_inventory()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_products_list(self, mock_post):
        """Test get_inventory_products_list method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "products": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_products_list(
            inventory_id=123,
            filter_name="laptop",
            filter_limit=10,
            filter_sort="name"
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryProductsList'

    def test_get_inventory_products_list_validation(self):
        """Test validation for get_inventory_products_list"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.get_inventory_products_list()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_products_data(self, mock_post):
        """Test get_inventory_products_data method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "products": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_products_data(
            inventory_id=123,
            products=["PROD-001", "PROD-002"]
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryProductsData'

    def test_get_inventory_products_data_validation(self):
        """Test validation for get_inventory_products_data"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.products.get_inventory_products_data()

        with pytest.raises(ValueError, match="Missing required parameters: products"):
            self.products.get_inventory_products_data(inventory_id=123)

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_products_stock(self, mock_post):
        """Test get_inventory_products_stock method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "products": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_products_stock(
            inventory_id=123,
            page=1
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryProductsStock'

    def test_get_inventory_products_stock_validation(self):
        """Test validation for get_inventory_products_stock"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.get_inventory_products_stock()

    @patch('baselinker.client.requests.Session.post')
    def test_add_inventory_product(self, mock_post):
        """Test add_inventory_product method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "product_id": "PROD-001"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.add_inventory_product(
            inventory_id=123,
            product_id="PROD-001",
            text_fields={"name": "Test Product"}
        )
        
        assert result["product_id"] == "PROD-001"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addInventoryProduct'

    def test_add_inventory_product_validation(self):
        """Test validation for add_inventory_product"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.products.add_inventory_product()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_inventory_product(self, mock_post):
        """Test delete_inventory_product method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.delete_inventory_product(
            inventory_id=123,
            product_id="PROD-001"
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteInventoryProduct'

    def test_delete_inventory_product_validation(self):
        """Test validation for delete_inventory_product"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.products.delete_inventory_product()

    @patch('baselinker.client.requests.Session.post')
    def test_update_inventory_products_stock(self, mock_post):
        """Test update_inventory_products_stock method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.update_inventory_products_stock(
            inventory_id=123,
            products=[{"product_id": "PROD-001", "stock": 100}]
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'updateInventoryProductsStock'

    def test_update_inventory_products_stock_validation(self):
        """Test validation for update_inventory_products_stock"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.products.update_inventory_products_stock()

    @patch('baselinker.client.requests.Session.post')
    def test_update_inventory_products_prices(self, mock_post):
        """Test update_inventory_products_prices method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.update_inventory_products_prices(
            inventory_id=123,
            products=[{"product_id": "PROD-001", "price_brutto": 29.99}]
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'updateInventoryProductsPrices'

    def test_update_inventory_products_prices_validation(self):
        """Test validation for update_inventory_products_prices"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.products.update_inventory_products_prices()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_categories(self, mock_post):
        """Test get_inventory_categories method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "categories": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_categories(inventory_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryCategories'

    def test_get_inventory_categories_validation(self):
        """Test validation for get_inventory_categories"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.get_inventory_categories()

    @patch('baselinker.client.requests.Session.post')
    def test_add_inventory_category(self, mock_post):
        """Test add_inventory_category method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "category_id": 456}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.add_inventory_category(
            inventory_id=123,
            name="Test Category",
            parent_id=0
        )
        
        assert result["category_id"] == 456
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addInventoryCategory'

    def test_add_inventory_category_validation(self):
        """Test validation for add_inventory_category"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.products.add_inventory_category()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_inventory_category(self, mock_post):
        """Test delete_inventory_category method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.delete_inventory_category(
            inventory_id=123,
            category_id=456
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteInventoryCategory'

    def test_delete_inventory_category_validation(self):
        """Test validation for delete_inventory_category"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.products.delete_inventory_category()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_manufacturers(self, mock_post):
        """Test get_inventory_manufacturers method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "manufacturers": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_manufacturers(inventory_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryManufacturers'

    def test_get_inventory_manufacturers_validation(self):
        """Test validation for get_inventory_manufacturers"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.get_inventory_manufacturers()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_tags(self, mock_post):
        """Test get_inventory_tags method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "tags": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_tags(inventory_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryTags'

    def test_get_inventory_tags_validation(self):
        """Test validation for get_inventory_tags"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.get_inventory_tags()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_extra_fields(self, mock_post):
        """Test get_inventory_extra_fields method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "fields": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_extra_fields(inventory_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryExtraFields'

    def test_get_inventory_extra_fields_validation(self):
        """Test validation for get_inventory_extra_fields"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.get_inventory_extra_fields()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_integrations(self, mock_post):
        """Test get_inventory_integrations method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "integrations": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_integrations(inventory_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryIntegrations'

    def test_get_inventory_integrations_validation(self):
        """Test validation for get_inventory_integrations"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.get_inventory_integrations()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_product_logs(self, mock_post):
        """Test get_inventory_product_logs method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "logs": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_product_logs(
            inventory_id=123,
            log_id=0,
            date_from=1640995200
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryProductLogs'

    def test_get_inventory_product_logs_validation(self):
        """Test validation for get_inventory_product_logs"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.get_inventory_product_logs()

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_available_text_field_keys(self, mock_post):
        """Test get_inventory_available_text_field_keys method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "text_field_keys": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_available_text_field_keys(inventory_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryAvailableTextFieldKeys'

    def test_get_inventory_available_text_field_keys_validation(self):
        """Test validation for get_inventory_available_text_field_keys"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.get_inventory_available_text_field_keys()

    @patch('baselinker.client.requests.Session.post')
    def test_run_inventory_products_macro(self, mock_post):
        """Test run_inventory_products_macro method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "logs": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.run_inventory_products_macro(
            inventory_id=123,
            macro_id=456,
            products=["PROD-001", "PROD-002"]
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'runInventoryProductsMacro'

    def test_run_inventory_products_macro_validation(self):
        """Test validation for run_inventory_products_macro"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.products.run_inventory_products_macro()

    @patch('baselinker.client.requests.Session.post')
    def test_sync_inventory_with_ai(self, mock_post):
        """Test sync_inventory_with_ai method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.sync_inventory_with_ai(
            inventory_id=123,
            mode="auto",
            product_ids=["PROD-001"]
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'syncInventoryWithAI'

    def test_sync_inventory_with_ai_validation(self):
        """Test validation for sync_inventory_with_ai"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.products.sync_inventory_with_ai()