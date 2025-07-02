import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient
from baselinker.exceptions import BaseLinkerError


class TestInventoryModuleComprehensive:
    """Comprehensive tests for InventoryModule"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.inventory = self.client.inventory

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_warehouses(self, mock_post):
        """Test get_inventory_warehouses method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "warehouses": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.inventory.get_inventory_warehouses(inventory_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryWarehouses'
        params = json.loads(call_args[1]['data']['parameters'])
        assert params['inventory_id'] == 123

    def test_get_inventory_warehouses_validation(self):
        """Test validation for get_inventory_warehouses"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.inventory.get_inventory_warehouses()

    @patch('baselinker.client.requests.Session.post')
    def test_add_inventory_warehouse(self, mock_post):
        """Test add_inventory_warehouse method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "warehouse_id": 456}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.inventory.add_inventory_warehouse(
            inventory_id=123,
            name="Test Warehouse",
            description="Test warehouse description",
            stock_edition=True,
            disable_stock_level_below_zero=True
        )
        
        assert result["warehouse_id"] == 456
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addInventoryWarehouse'
        params = json.loads(call_args[1]['data']['parameters'])
        assert params['inventory_id'] == 123
        assert params['name'] == "Test Warehouse"
        assert params['stock_edition'] == True

    def test_add_inventory_warehouse_validation(self):
        """Test validation for add_inventory_warehouse"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.inventory.add_inventory_warehouse()

        with pytest.raises(ValueError, match="Missing required parameters"):
            self.inventory.add_inventory_warehouse(inventory_id=123)

        with pytest.raises(ValueError, match="Missing required parameters: name"):
            self.inventory.add_inventory_warehouse(inventory_id=123, description="test")

    @patch('baselinker.client.requests.Session.post')
    def test_delete_inventory_warehouse(self, mock_post):
        """Test delete_inventory_warehouse method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.inventory.delete_inventory_warehouse(
            inventory_id=123,
            warehouse_id=456
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteInventoryWarehouse'
        params = json.loads(call_args[1]['data']['parameters'])
        assert params['inventory_id'] == 123
        assert params['warehouse_id'] == 456

    def test_delete_inventory_warehouse_validation(self):
        """Test validation for delete_inventory_warehouse"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.inventory.delete_inventory_warehouse()

        with pytest.raises(ValueError, match="Missing required parameters"):
            self.inventory.delete_inventory_warehouse(inventory_id=123)

    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_price_groups(self, mock_post):
        """Test get_inventory_price_groups method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "price_groups": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.inventory.get_inventory_price_groups(inventory_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryPriceGroups'
        params = json.loads(call_args[1]['data']['parameters'])
        assert params['inventory_id'] == 123

    def test_get_inventory_price_groups_validation(self):
        """Test validation for get_inventory_price_groups"""
        with pytest.raises(ValueError, match="Missing required parameters: inventory_id"):
            self.inventory.get_inventory_price_groups()

    @patch('baselinker.client.requests.Session.post')
    def test_add_inventory_price_group(self, mock_post):
        """Test add_inventory_price_group method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "price_group_id": 789}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.inventory.add_inventory_price_group(
            inventory_id=123,
            name="Test Price Group",
            description="Test price group description",
            currency="PLN",
            is_default=False
        )
        
        assert result["price_group_id"] == 789
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addInventoryPriceGroup'
        params = json.loads(call_args[1]['data']['parameters'])
        assert params['inventory_id'] == 123
        assert params['name'] == "Test Price Group"
        assert params['currency'] == "PLN"

    def test_add_inventory_price_group_validation(self):
        """Test validation for add_inventory_price_group"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.inventory.add_inventory_price_group()

        with pytest.raises(ValueError, match="Missing required parameters"):
            self.inventory.add_inventory_price_group(inventory_id=123)

        with pytest.raises(ValueError, match="Missing required parameters: name"):
            self.inventory.add_inventory_price_group(inventory_id=123, currency="PLN")

    @patch('baselinker.client.requests.Session.post')
    def test_delete_inventory_price_group(self, mock_post):
        """Test delete_inventory_price_group method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.inventory.delete_inventory_price_group(
            inventory_id=123,
            price_group_id=789
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteInventoryPriceGroup'
        params = json.loads(call_args[1]['data']['parameters'])
        assert params['inventory_id'] == 123
        assert params['price_group_id'] == 789

    def test_delete_inventory_price_group_validation(self):
        """Test validation for delete_inventory_price_group"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.inventory.delete_inventory_price_group()

        with pytest.raises(ValueError, match="Missing required parameters"):
            self.inventory.delete_inventory_price_group(inventory_id=123)

    @patch('baselinker.client.requests.Session.post')
    def test_inventory_warehouse_complex_scenarios(self, mock_post):
        """Test complex warehouse management scenarios"""
        # Test with all optional parameters
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "warehouse_id": 999}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.inventory.add_inventory_warehouse(
            inventory_id=123,
            name="Complex Warehouse",
            description="Warehouse with all features",
            stock_edition=True,
            disable_stock_level_below_zero=False
        )
        
        assert result["warehouse_id"] == 999
        params = json.loads(mock_post.call_args[1]['data']['parameters'])
        assert params['disable_stock_level_below_zero'] == False

    @patch('baselinker.client.requests.Session.post')
    def test_inventory_price_group_complex_scenarios(self, mock_post):
        """Test complex price group management scenarios"""
        # Test with all optional parameters
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "price_group_id": 888}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.inventory.add_inventory_price_group(
            inventory_id=123,
            name="Premium Price Group",
            description="Premium customer pricing",
            currency="EUR",
            is_default=True
        )
        
        assert result["price_group_id"] == 888
        params = json.loads(mock_post.call_args[1]['data']['parameters'])
        assert params['is_default'] == True
        assert params['currency'] == "EUR"

    @patch('baselinker.client.requests.Session.post')
    def test_error_handling_scenarios(self, mock_post):
        """Test error handling in inventory operations"""
        # Test API error response
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_INVENTORY_NOT_FOUND",
            "error_message": "Inventory not found"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        with pytest.raises(BaseLinkerError):
            self.inventory.get_inventory_warehouses(inventory_id=999999)

    def test_parameter_edge_cases(self):
        """Test edge cases for parameter validation"""
        # Test with empty strings
        with pytest.raises(ValueError):
            self.inventory.add_inventory_warehouse(
                inventory_id=123,
                name="",  # Empty name should fail
                description="test"
            )

        # Test with None values
        with pytest.raises(ValueError):
            self.inventory.add_inventory_price_group(
                inventory_id=123,
                name=None,
                description="test"
            )

        # Test with invalid types
        with pytest.raises(ValueError):
            self.inventory.get_inventory_warehouses(inventory_id="invalid")