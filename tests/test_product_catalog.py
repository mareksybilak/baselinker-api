import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestProductCatalog:
    
    @patch('requests.Session.post')
    def test_get_inventory_products_data(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "products": [
                {
                    "product_id": "ABC123",
                    "name": "Test Product",
                    "price_netto": 19.99,
                    "stock": 50
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.products.get_inventory_products_data(
            inventory_id=123,
            products=["ABC123"]
        )
        
        assert "products" in result
        assert len(result["products"]) == 1
        assert result["products"][0]["product_id"] == "ABC123"
        
        expected_data = {
            'method': 'getInventoryProductsData',
            'parameters': json.dumps({
                "inventory_id": 123,
                "products": ["ABC123"]
            })
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_delete_inventory_product(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.products.delete_inventory_product(
            inventory_id=123,
            product_id="ABC123"
        )
        
        assert result["status"] == "SUCCESS"
        
        expected_data = {
            'method': 'deleteInventoryProduct',
            'parameters': json.dumps({
                "inventory_id": 123,
                "product_id": "ABC123"
            })
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_update_inventory_products_stock(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "warnings": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        stock_data = {
            "inventory_id": 123,
            "products": [
                {"product_id": "ABC123", "variant_id": 0, "stock": 25},
                {"product_id": "DEF456", "variant_id": 0, "stock": 30}
            ]
        }
        result = client.products.update_inventory_products_stock(**stock_data)
        
        assert result["status"] == "SUCCESS"
        assert "warnings" in result
    
    @patch('requests.Session.post')
    def test_update_inventory_products_prices(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "warnings": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        price_data = {
            "inventory_id": 123,
            "products": [
                {
                    "product_id": "ABC123",
                    "variant_id": 0,
                    "price_netto": 24.99,
                    "price_brutto": 30.74
                }
            ]
        }
        result = client.products.update_inventory_products_prices(**price_data)
        
        assert result["status"] == "SUCCESS"
    
    @patch('requests.Session.post')
    def test_get_inventory_categories(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "categories": [
                {"category_id": 1, "name": "Electronics", "parent_id": 0},
                {"category_id": 2, "name": "Phones", "parent_id": 1}
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.products.get_inventory_categories(inventory_id=123)
        
        assert "categories" in result
        assert len(result["categories"]) == 2
        assert result["categories"][0]["name"] == "Electronics"
    
    @patch('requests.Session.post')
    def test_add_inventory_category(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "category_id": 3}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        category_data = {
            "inventory_id": 123,
            "name": "New Category",
            "parent_id": 1
        }
        result = client.products.add_inventory_category(**category_data)
        
        assert result["status"] == "SUCCESS"
        assert result["category_id"] == 3
    
    @patch('requests.Session.post')
    def test_delete_inventory_category(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.products.delete_inventory_category(
            inventory_id=123,
            category_id=3
        )
        
        assert result["status"] == "SUCCESS"
    
    @patch('requests.Session.post')
    def test_add_inventory(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "inventory_id": 456}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        inventory_data = {
            "name": "New Inventory",
            "description": "Test inventory",
            "languages": ["pl", "en"]
        }
        result = client.products.add_inventory(**inventory_data)
        
        assert result["status"] == "SUCCESS"
        assert result["inventory_id"] == 456
    
    @patch('requests.Session.post')
    def test_delete_inventory(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.products.delete_inventory(inventory_id=456)
        
        assert result["status"] == "SUCCESS"
        
        expected_data = {
            'method': 'deleteInventory',
            'parameters': json.dumps({"inventory_id": 456})
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )