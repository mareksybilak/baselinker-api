import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestExternalStorage:
    
    @patch('requests.Session.post')
    def test_get_external_storages_list(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "storages": [
                {
                    "storage_id": "allegro_123",
                    "name": "Allegro Store",
                    "type": "allegro",
                    "status": "active"
                },
                {
                    "storage_id": "ebay_456",
                    "name": "eBay Store",
                    "type": "ebay",
                    "status": "active"
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.external_storage.get_external_storages_list()
        
        assert "storages" in result
        assert len(result["storages"]) == 2
        assert result["storages"][0]["type"] == "allegro"
        assert result["storages"][1]["name"] == "eBay Store"
        
        expected_data = {
            'method': 'getExternalStoragesList',
            'parameters': json.dumps({})
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_get_external_storage_products_data(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "products": [
                {
                    "product_id": "EXT123",
                    "name": "External Product 1",
                    "price": 29.99,
                    "quantity": 10,
                    "storage_id": "allegro_123"
                },
                {
                    "product_id": "EXT456",
                    "name": "External Product 2",
                    "price": 49.99,
                    "quantity": 5,
                    "storage_id": "allegro_123"
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.external_storage.get_external_storage_products_data(
            storage_id="allegro_123",
            products=["EXT123", "EXT456"]
        )
        
        assert "products" in result
        assert len(result["products"]) == 2
        assert result["products"][0]["storage_id"] == "allegro_123"
        
        expected_data = {
            'method': 'getExternalStorageProductsData',
            'parameters': json.dumps({
                "storage_id": "allegro_123",
                "products": ["EXT123", "EXT456"]
            })
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_get_external_storage_products_quantity(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "products": [
                {
                    "product_id": "EXT123",
                    "variants": [
                        {"variant_id": "VAR1", "stock": 15},
                        {"variant_id": "VAR2", "stock": 8}
                    ]
                },
                {
                    "product_id": "EXT456",
                    "variants": [
                        {"variant_id": "VAR3", "stock": 22}
                    ]
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.external_storage.get_external_storage_products_quantity(
            storage_id="allegro_123",
            products=["EXT123", "EXT456"]
        )
        
        assert "products" in result
        assert len(result["products"]) == 2
        assert len(result["products"][0]["variants"]) == 2
        assert result["products"][0]["variants"][0]["stock"] == 15
    
    @patch('requests.Session.post')
    def test_update_external_storage_products_quantity(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "SUCCESS",
            "warnings": [],
            "updated_products": 2
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        update_data = {
            "storage_id": "allegro_123",
            "products": [
                {
                    "product_id": "EXT123",
                    "variants": [
                        {"variant_id": "VAR1", "stock": 20},
                        {"variant_id": "VAR2", "stock": 12}
                    ]
                },
                {
                    "product_id": "EXT456",
                    "variants": [
                        {"variant_id": "VAR3", "stock": 25}
                    ]
                }
            ]
        }
        result = client.external_storage.update_external_storage_products_quantity(**update_data)
        
        assert result["status"] == "SUCCESS"
        assert result["updated_products"] == 2
        assert "warnings" in result
        
        expected_data = {
            'method': 'updateExternalStorageProductsQuantity',
            'parameters': json.dumps(update_data)
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_external_storage_with_filtering(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "products": [
                {
                    "product_id": "FILTERED123",
                    "name": "Filtered Product",
                    "price": 99.99,
                    "quantity": 3,
                    "category": "electronics"
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.external_storage.get_external_storage_products_data(
            storage_id="ebay_456",
            products=["FILTERED123"],
            filter_category_id="electronics",
            filter_name="laptop",
            filter_price_from=50.00,
            filter_price_to=150.00,
            filter_quantity_from=1
        )
        
        assert "products" in result
        assert len(result["products"]) == 1
        assert result["products"][0]["category"] == "electronics"
    
    @patch('requests.Session.post')
    def test_external_storage_bulk_quantity_update(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "SUCCESS",
            "warnings": [
                "Product EXT999 not found in storage"
            ],
            "updated_products": 4,
            "failed_products": 1
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        bulk_update = {
            "storage_id": "allegro_123",
            "products": [
                {"product_id": "EXT001", "variants": [{"variant_id": "V1", "stock": 100}]},
                {"product_id": "EXT002", "variants": [{"variant_id": "V2", "stock": 200}]},
                {"product_id": "EXT003", "variants": [{"variant_id": "V3", "stock": 150}]},
                {"product_id": "EXT004", "variants": [{"variant_id": "V4", "stock": 75}]},
                {"product_id": "EXT999", "variants": [{"variant_id": "V5", "stock": 50}]}
            ]
        }
        result = client.external_storage.update_external_storage_products_quantity(**bulk_update)
        
        assert result["status"] == "SUCCESS"
        assert result["updated_products"] == 4
        assert result["failed_products"] == 1
        assert len(result["warnings"]) == 1
        assert "EXT999 not found" in result["warnings"][0]