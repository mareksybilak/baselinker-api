import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient
from baselinker.exceptions import BaseLinkerError


class TestCourierModuleComprehensive:
    """Comprehensive tests for CourierModule"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.courier = self.client.courier

    @patch('baselinker.client.requests.Session.post')
    def test_get_couriers_list(self, mock_post):
        """Test get_couriers_list method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "couriers": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_couriers_list()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getCouriersList'

    @patch('baselinker.client.requests.Session.post')
    def test_get_courier_services(self, mock_post):
        """Test get_courier_services method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "services": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_courier_services(courier_code="dpd")
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getCourierServices'
        params = json.loads(call_args[1]['data']['parameters'])
        assert params['courier_code'] == "dpd"

    def test_get_courier_services_validation(self):
        """Test validation for get_courier_services"""
        with pytest.raises(ValueError, match="Missing required parameters: courier_code"):
            self.courier.get_courier_services()

    @patch('baselinker.client.requests.Session.post')
    def test_get_courier_fields(self, mock_post):
        """Test get_courier_fields method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "fields": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_courier_fields(courier_code="dpd")
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getCourierFields'

    def test_get_courier_fields_validation(self):
        """Test validation for get_courier_fields"""
        with pytest.raises(ValueError, match="Missing required parameters: courier_code"):
            self.courier.get_courier_fields()

    @patch('baselinker.client.requests.Session.post')
    def test_get_courier_packages_status_history(self, mock_post):
        """Test get_courier_packages_status_history method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "history": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_courier_packages_status_history(date_from=1640995200)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getCourierPackagesStatusHistory'

    def test_get_courier_packages_status_history_validation(self):
        """Test validation for get_courier_packages_status_history"""
        with pytest.raises(ValueError, match="Missing required parameters: date_from"):
            self.courier.get_courier_packages_status_history()

    @patch('baselinker.client.requests.Session.post')
    def test_create_package(self, mock_post):
        """Test create_package method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "package_id": 123}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.create_package(
            order_id=12345,
            courier_code="dpd",
            fields={"weight": 2.5, "size": "M"}
        )
        
        assert result["package_id"] == 123
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'createPackage'

    def test_create_package_validation(self):
        """Test validation for create_package"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.courier.create_package()

    @patch('baselinker.client.requests.Session.post')
    def test_create_package_manual(self, mock_post):
        """Test create_package_manual method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "package_id": 456}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.create_package_manual(
            order_id=12345,
            courier_code="dpd",
            package_number="123456789",
            pickup_date="2024-01-15"
        )
        
        assert result["package_id"] == 456
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'createPackageManual'

    def test_create_package_manual_validation(self):
        """Test validation for create_package_manual"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.courier.create_package_manual()

    @patch('baselinker.client.requests.Session.post')
    def test_get_label(self, mock_post):
        """Test get_label method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "label": "base64data"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_label(
            package_id=123,
            label_type="normal"
        )
        
        assert result["label"] == "base64data"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getLabel'

    def test_get_label_validation(self):
        """Test validation for get_label"""
        with pytest.raises(ValueError, match="Missing required parameters: package_id"):
            self.courier.get_label()

    @patch('baselinker.client.requests.Session.post')
    def test_get_order_packages(self, mock_post):
        """Test get_order_packages method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "packages": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_order_packages(order_id=12345)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderPackages'

    def test_get_order_packages_validation(self):
        """Test validation for get_order_packages"""
        with pytest.raises(ValueError, match="Missing required parameters: order_id"):
            self.courier.get_order_packages()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_order_package(self, mock_post):
        """Test delete_order_package method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.delete_order_package(package_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteOrderPackage'

    def test_delete_order_package_validation(self):
        """Test validation for delete_order_package"""
        with pytest.raises(ValueError, match="Missing required parameters: package_id"):
            self.courier.delete_order_package()

    @patch('baselinker.client.requests.Session.post')
    def test_request_parcel_pickup(self, mock_post):
        """Test request_parcel_pickup method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "pickup_id": 789}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.request_parcel_pickup(
            courier_code="dpd",
            package_ids=[123, 456],
            pickup_date="2024-01-15"
        )
        
        assert result["pickup_id"] == 789
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'requestParcelPickup'

    def test_request_parcel_pickup_validation(self):
        """Test validation for request_parcel_pickup"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.courier.request_parcel_pickup()

    @patch('baselinker.client.requests.Session.post')
    def test_get_courier_accounts(self, mock_post):
        """Test get_courier_accounts method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "accounts": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_courier_accounts()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getCourierAccounts'

    @patch('baselinker.client.requests.Session.post')
    def test_get_package_status(self, mock_post):
        """Test get_package_status method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "package_status": "delivered"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_package_status(package_id=123)
        
        assert result["package_status"] == "delivered"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getPackageStatus'

    def test_get_package_status_validation(self):
        """Test validation for get_package_status"""
        with pytest.raises(ValueError, match="Missing required parameters: package_id"):
            self.courier.get_package_status()

    @patch('baselinker.client.requests.Session.post')
    def test_complex_package_creation(self, mock_post):
        """Test complex package creation with all parameters"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "package_id": 999}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        complex_fields = {
            "weight": 2.5,
            "size": "L",
            "width": 30,
            "height": 20,
            "length": 40,
            "declared_content": "Electronics",
            "insurance": True,
            "insurance_value": 500.00,
            "cod": False,
            "delivery_point_id": "DPD_001"
        }
        
        result = self.courier.create_package(
            order_id=12345,
            courier_code="dpd",
            fields=complex_fields
        )
        
        assert result["package_id"] == 999
        params = json.loads(mock_post.call_args[1]['data']['parameters'])
        assert params['fields']['insurance'] == True
        assert params['fields']['weight'] == 2.5

    @patch('baselinker.client.requests.Session.post')
    def test_label_with_options(self, mock_post):
        """Test label generation with different options"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "label": "base64data"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_label(
            package_id=123,
            label_type="thermal",
            label_format="pdf"
        )
        
        assert result["label"] == "base64data"
        params = json.loads(mock_post.call_args[1]['data']['parameters'])
        assert params['label_type'] == "thermal"
        assert params['label_format'] == "pdf"

    @patch('baselinker.client.requests.Session.post')
    def test_pickup_with_detailed_info(self, mock_post):
        """Test parcel pickup with detailed information"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "pickup_id": 888}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.request_parcel_pickup(
            courier_code="ups",
            package_ids=[123, 456, 789],
            pickup_date="2024-01-15",
            pickup_time_from="10:00",
            pickup_time_to="16:00",
            address={
                "name": "Company Name",
                "street": "Test Street 123",
                "city": "Warsaw",
                "postcode": "00-001",
                "country": "PL",
                "phone": "+48123456789",
                "email": "contact@company.com"
            }
        )
        
        assert result["pickup_id"] == 888
        params = json.loads(mock_post.call_args[1]['data']['parameters'])
        assert len(params['package_ids']) == 3
        assert params['address']['city'] == "Warsaw"

    @patch('baselinker.client.requests.Session.post')
    def test_error_scenarios(self, mock_post):
        """Test various error scenarios"""
        # Test invalid courier code
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_INVALID_COURIER",
            "error_message": "Invalid courier code"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        with pytest.raises(BaseLinkerError):
            self.courier.get_courier_services(courier_code="invalid_courier")

    def test_parameter_edge_cases(self):
        """Test edge cases for parameter validation"""
        # Test empty courier code
        with pytest.raises(ValueError):
            self.courier.get_courier_services(courier_code="")
        
        # Test invalid package_ids type
        with pytest.raises(ValueError):
            self.courier.request_parcel_pickup(
                courier_code="dpd",
                package_ids="invalid",  # Should be list
                pickup_date="2024-01-15"
            )