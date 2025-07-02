import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestDevicesModuleComprehensive:
    """Comprehensive tests for DevicesModule"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.devices = self.client.devices

    @patch('baselinker.client.requests.Session.post')
    def test_get_connect_integrations(self, mock_post):
        """Test get_connect_integrations method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "integrations": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.get_connect_integrations()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getConnectIntegrations'

    @patch('baselinker.client.requests.Session.post')
    def test_add_connect_integration(self, mock_post):
        """Test add_connect_integration method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "integration_id": 123}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.add_connect_integration(
            name="Test Integration",
            type="api",
            config={"url": "https://api.example.com"}
        )
        
        assert result["integration_id"] == 123
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addConnectIntegration'

    def test_add_connect_integration_validation(self):
        """Test validation for add_connect_integration"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.devices.add_connect_integration()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_connect_integration(self, mock_post):
        """Test delete_connect_integration method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.delete_connect_integration(integration_id=123)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteConnectIntegration'

    def test_delete_connect_integration_validation(self):
        """Test validation for delete_connect_integration"""
        with pytest.raises(ValueError, match="Missing required parameters: integration_id"):
            self.devices.delete_connect_integration()

    @patch('baselinker.client.requests.Session.post')
    def test_get_printers(self, mock_post):
        """Test get_printers method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "printers": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.get_printers()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getPrinters'

    @patch('baselinker.client.requests.Session.post')
    def test_add_printer(self, mock_post):
        """Test add_printer method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "printer_id": 456}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.add_printer(
            name="Test Printer",
            type="thermal",
            connection="usb"
        )
        
        assert result["printer_id"] == 456
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addPrinter'

    def test_add_printer_validation(self):
        """Test validation for add_printer"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.devices.add_printer()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_printer(self, mock_post):
        """Test delete_printer method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.delete_printer(printer_id=456)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deletePrinter'

    def test_delete_printer_validation(self):
        """Test validation for delete_printer"""
        with pytest.raises(ValueError, match="Missing required parameters: printer_id"):
            self.devices.delete_printer()

    @patch('baselinker.client.requests.Session.post')
    def test_get_scales(self, mock_post):
        """Test get_scales method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "scales": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.get_scales()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getScales'

    @patch('baselinker.client.requests.Session.post')
    def test_add_scale(self, mock_post):
        """Test add_scale method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "scale_id": 789}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.add_scale(
            name="Test Scale",
            type="digital",
            connection="serial"
        )
        
        assert result["scale_id"] == 789
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addScale'

    def test_add_scale_validation(self):
        """Test validation for add_scale"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.devices.add_scale()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_scale(self, mock_post):
        """Test delete_scale method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.delete_scale(scale_id=789)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteScale'

    def test_delete_scale_validation(self):
        """Test validation for delete_scale"""
        with pytest.raises(ValueError, match="Missing required parameters: scale_id"):
            self.devices.delete_scale()

    @patch('baselinker.client.requests.Session.post')
    def test_get_scanners(self, mock_post):
        """Test get_scanners method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "scanners": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.get_scanners()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getScanners'

    @patch('baselinker.client.requests.Session.post')
    def test_add_scanner(self, mock_post):
        """Test add_scanner method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "scanner_id": 101}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.add_scanner(
            name="Test Scanner",
            type="barcode",
            connection="usb"
        )
        
        assert result["scanner_id"] == 101
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addScanner'

    def test_add_scanner_validation(self):
        """Test validation for add_scanner"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.devices.add_scanner()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_scanner(self, mock_post):
        """Test delete_scanner method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.delete_scanner(scanner_id=101)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteScanner'

    def test_delete_scanner_validation(self):
        """Test validation for delete_scanner"""
        with pytest.raises(ValueError, match="Missing required parameters: scanner_id"):
            self.devices.delete_scanner()

    @patch('baselinker.client.requests.Session.post')
    def test_get_automation_rules(self, mock_post):
        """Test get_automation_rules method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "rules": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.get_automation_rules()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getAutomationRules'

    @patch('baselinker.client.requests.Session.post')
    def test_add_automation_rule(self, mock_post):
        """Test add_automation_rule method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "rule_id": 202}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.add_automation_rule(
            name="Test Rule",
            trigger="order_status_change",
            action="send_email"
        )
        
        assert result["rule_id"] == 202
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addAutomationRule'

    def test_add_automation_rule_validation(self):
        """Test validation for add_automation_rule"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.devices.add_automation_rule()

    @patch('baselinker.client.requests.Session.post')
    def test_delete_automation_rule(self, mock_post):
        """Test delete_automation_rule method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.delete_automation_rule(rule_id=202)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'deleteAutomationRule'

    def test_delete_automation_rule_validation(self):
        """Test validation for delete_automation_rule"""
        with pytest.raises(ValueError, match="Missing required parameters: rule_id"):
            self.devices.delete_automation_rule()

    @patch('baselinker.client.requests.Session.post')
    def test_get_device_logs(self, mock_post):
        """Test get_device_logs method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "logs": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.devices.get_device_logs(
            device_type="printer",
            date_from=1640995200
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getDeviceLogs'

    def test_get_device_logs_validation(self):
        """Test validation for get_device_logs"""
        with pytest.raises(ValueError, match="Missing required parameters: device_type"):
            self.devices.get_device_logs()