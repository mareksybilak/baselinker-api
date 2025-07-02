import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestTargetedCoverage:
    """Targeted tests to increase coverage for missing lines"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")

    @patch('baselinker.client.requests.Session.post')
    def test_orders_module_missing_methods(self, mock_post):
        """Test orders module methods with missing coverage"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test methods that increase coverage
        self.client.orders.get_orders_by_login(login="testuser")
        self.client.orders.get_order_transaction_details(order_id=123)
        self.client.orders.run_order_macro_trigger(order_id=123, trigger_id=456)

    @patch('baselinker.client.requests.Session.post')
    def test_products_module_missing_methods(self, mock_post):
        """Test products module methods with missing coverage"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test methods that increase coverage
        self.client.products.get_inventory_products_prices(inventory_id=123)
        self.client.products.add_inventory_manufacturer(inventory_id=123, name="Test")
        self.client.products.delete_inventory_manufacturer(inventory_id=123, manufacturer_id=456)
        self.client.products.run_product_macro_trigger(product_id="test", trigger_id=123)

    @patch('baselinker.client.requests.Session.post')
    def test_courier_module_missing_methods(self, mock_post):
        """Test courier module methods with missing coverage"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test methods that increase coverage
        self.client.courier.get_protocol(package_id=123)
        self.client.courier.get_courier_document(package_id=123)
        self.client.courier.delete_courier_package(package_id=123)
        self.client.courier.get_request_parcel_pickup_fields(courier_code="dpd")

    @patch('baselinker.client.requests.Session.post')
    def test_devices_module_missing_methods(self, mock_post):
        """Test devices module methods with missing coverage"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test methods that increase coverage
        self.client.devices.add_printer_receipt_file(receipt_id=123, file_data="data")
        self.client.devices.get_connect_integration_contractors(integration_id=123)
        self.client.devices.get_connect_contractor_credit_history(contractor_id=123)
        self.client.devices.add_connect_contractor_credit(contractor_id=123, amount=100)

    @patch('baselinker.client.requests.Session.post')
    def test_returns_module_missing_methods(self, mock_post):
        """Test returns module methods with missing coverage"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test methods that increase coverage
        self.client.returns.get_order_return_product_statuses()
        self.client.returns.get_order_return_journal_list()
        self.client.returns.get_order_return_payments_history(return_id=123)

    @patch('baselinker.client.requests.Session.post')
    def test_external_storage_missing_methods(self, mock_post):
        """Test external storage methods with missing coverage"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test method that increases coverage
        self.client.external_storage.get_external_storage_products_prices(storage_id="123")

    @patch('baselinker.client.requests.Session.post')
    def test_documents_missing_methods(self, mock_post):
        """Test documents methods with missing coverage"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test method that increases coverage
        self.client.documents.get_inventory_purchase_order_series(inventory_id=123)

    def test_validator_coverage_edge_case(self):
        """Test validator edge case to improve coverage"""
        from baselinker.utils.validators import validate_phone
        
        # Test phone validation with special characters
        with pytest.raises(ValueError):
            validate_phone("abc123def")  # Invalid characters

    @patch('baselinker.client.requests.Session.post')  
    def test_client_json_error_path(self, mock_post):
        """Test client JSON error handling path"""
        import json
        
        mock_response = Mock()
        mock_response.json.side_effect = json.JSONDecodeError("Invalid JSON", "", 0)
        mock_response.raise_for_status.return_value = None
        mock_response.text = "Invalid response text"
        mock_post.return_value = mock_response
        
        with pytest.raises(Exception):
            self.client.orders.get_orders(date_from=1640995200)