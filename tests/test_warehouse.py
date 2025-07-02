import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestWarehouse:
    
    @patch('requests.Session.post')
    def test_get_inventory_warehouses(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "warehouses": [
                {
                    "warehouse_id": 1,
                    "name": "Main Warehouse",
                    "description": "Primary storage location"
                },
                {
                    "warehouse_id": 2,
                    "name": "Secondary Warehouse",
                    "description": "Backup storage"
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.inventory.get_inventory_warehouses(inventory_id=123)
        
        assert "warehouses" in result
        assert len(result["warehouses"]) == 2
        assert result["warehouses"][0]["name"] == "Main Warehouse"
        
        expected_data = {
            'method': 'getInventoryWarehouses',
            'parameters': json.dumps({"inventory_id": 123})
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_add_inventory_warehouse(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "SUCCESS",
            "warehouse_id": 3
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        warehouse_data = {
            "inventory_id": 123,
            "warehouse_id": "new_wh_001",
            "name": "New Warehouse",
            "description": "Additional storage facility",
            "stock_edition": True
        }
        result = client.inventory.add_inventory_warehouse(**warehouse_data)
        
        assert result["status"] == "SUCCESS"
        assert result["warehouse_id"] == 3
        
        expected_data = {
            'method': 'addInventoryWarehouse',
            'parameters': json.dumps(warehouse_data)
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_delete_inventory_warehouse(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.inventory.delete_inventory_warehouse(
            inventory_id=123,
            warehouse_id=3
        )
        
        assert result["status"] == "SUCCESS"
        
        expected_data = {
            'method': 'deleteInventoryWarehouse',
            'parameters': json.dumps({
                "inventory_id": 123,
                "warehouse_id": 3
            })
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_get_inventory_price_groups(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "price_groups": [
                {
                    "price_group_id": 1,
                    "name": "Retail",
                    "description": "Standard retail prices"
                },
                {
                    "price_group_id": 2,
                    "name": "Wholesale",
                    "description": "Bulk pricing"
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.inventory.get_inventory_price_groups(inventory_id=123)
        
        assert "price_groups" in result
        assert len(result["price_groups"]) == 2
        assert result["price_groups"][0]["name"] == "Retail"
    
    @patch('requests.Session.post')
    def test_add_inventory_price_group(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "SUCCESS",
            "price_group_id": 3
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        price_group_data = {
            "inventory_id": 123,
            "price_group_id": 3,
            "name": "VIP Pricing",
            "description": "Special pricing for VIP customers",
            "currency": "PLN"
        }
        result = client.inventory.add_inventory_price_group(**price_group_data)
        
        assert result["status"] == "SUCCESS"
        assert result["price_group_id"] == 3
    
    @patch('requests.Session.post')
    def test_delete_inventory_price_group(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.inventory.delete_inventory_price_group(
            inventory_id=123,
            price_group_id=3
        )
        
        assert result["status"] == "SUCCESS"
        
        expected_data = {
            'method': 'deleteInventoryPriceGroup',
            'parameters': json.dumps({
                "inventory_id": 123,
                "price_group_id": 3
            })
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_warehouse_operations_with_complex_data(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        
        # Test adding warehouse with all optional parameters
        complex_warehouse_data = {
            "inventory_id": 123,
            "warehouse_id": "complex_wh_001",
            "name": "Complex Warehouse",
            "description": "Full featured warehouse",
            "stock_edition": True,
            "is_default": False,
            "disable_stock_level_below_zero": True
        }
        result = client.inventory.add_inventory_warehouse(**complex_warehouse_data)
        assert result["status"] == "SUCCESS"
        
        # Test price group with currency and discount settings
        complex_price_group = {
            "inventory_id": 123,
            "price_group_id": 5,
            "name": "Premium Group",
            "description": "Premium customer pricing",
            "currency": "EUR",
            "price_modifier_percent": -10
        }
        result = client.inventory.add_inventory_price_group(**complex_price_group)
        assert result["status"] == "SUCCESS"