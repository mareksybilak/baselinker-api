import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestCourier:
    
    @patch('requests.Session.post')
    def test_create_package_manual(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "SUCCESS",
            "package_id": 789,
            "package_number": "PKG123456789"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        package_data = {
            "order_id": 123,
            "courier_code": "DPD",
            "package_number": "PKG123456789",
            "fields": {
                "size": "M",
                "weight": 2.5,
                "width": 20,
                "height": 15,
                "length": 30
            }
        }
        result = client.courier.create_package_manual(**package_data)
        
        assert result["status"] == "SUCCESS"
        assert result["package_id"] == 789
        assert result["package_number"] == "PKG123456789"
        
        expected_data = {
            'method': 'createPackageManual',
            'parameters': json.dumps(package_data)
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_get_label(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "SUCCESS",
            "label": "base64_encoded_label_data_here...",
            "label_format": "PDF"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.courier.get_label(package_id=789)
        
        assert result["status"] == "SUCCESS"
        assert "label" in result
        assert result["label_format"] == "PDF"
        
        expected_data = {
            'method': 'getLabel',
            'parameters': json.dumps({"package_id": 789})
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_get_order_packages(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "packages": [
                {
                    "package_id": 789,
                    "package_number": "PKG123456789",
                    "courier_code": "DPD",
                    "status": "created",
                    "tracking_number": "1234567890"
                },
                {
                    "package_id": 790,
                    "package_number": "PKG987654321",
                    "courier_code": "UPS",
                    "status": "shipped",
                    "tracking_number": "0987654321"
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.courier.get_order_packages(order_id=123)
        
        assert "packages" in result
        assert len(result["packages"]) == 2
        assert result["packages"][0]["courier_code"] == "DPD"
        assert result["packages"][1]["status"] == "shipped"
    
    @patch('requests.Session.post')
    def test_request_parcel_pickup(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "SUCCESS",
            "pickup_id": "PICKUP123",
            "pickup_date": "2023-12-01",
            "pickup_time": "14:00-16:00"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        pickup_data = {
            "courier_code": "DPD",
            "package_ids": [789, 790],
            "pickup_date": "2023-12-01",
            "pickup_time_from": "14:00",
            "pickup_time_to": "16:00",
            "address": {
                "name": "Test Company",
                "street": "Test Street 123",
                "city": "Warsaw",
                "postcode": "00-001",
                "country": "PL"
            }
        }
        result = client.courier.request_parcel_pickup(**pickup_data)
        
        assert result["status"] == "SUCCESS"
        assert result["pickup_id"] == "PICKUP123"
        assert result["pickup_date"] == "2023-12-01"
    
    @patch('requests.Session.post')
    def test_create_package_with_comprehensive_data(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "SUCCESS",
            "package_id": 791,
            "package_number": "PKG111222333",
            "tracking_number": "TRK999888777"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        comprehensive_package = {
            "order_id": 124,
            "courier_code": "INPOST",
            "package_number": "PKG111222333",
            "fields": {
                "size": "L",
                "weight": 5.0,
                "width": 40,
                "height": 30,
                "length": 50,
                "declared_content": "Electronics",
                "insurance": True,
                "insurance_value": 500.00,
                "cod_amount": 299.99,
                "delivery_confirmation": True
            },
            "receiver": {
                "name": "John Doe",
                "company": "Test Company Ltd",
                "street": "Main Street 456",
                "city": "Krakow",
                "postcode": "30-001",
                "country": "PL",
                "phone": "+48123456789",
                "email": "john@example.com"
            }
        }
        result = client.courier.create_package_manual(**comprehensive_package)
        
        assert result["status"] == "SUCCESS"
        assert result["package_id"] == 791
        assert "tracking_number" in result
    
    @patch('requests.Session.post')
    def test_get_label_with_format_options(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "SUCCESS",
            "label": "base64_encoded_label_data...",
            "label_format": "ZPL",
            "label_size": "100x150mm"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.courier.get_label(
            package_id=789,
            label_format="ZPL",
            label_size="100x150mm"
        )
        
        assert result["status"] == "SUCCESS"
        assert result["label_format"] == "ZPL"
        assert result["label_size"] == "100x150mm"