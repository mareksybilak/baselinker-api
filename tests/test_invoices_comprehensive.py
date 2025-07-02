import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestInvoicesModuleComprehensive:
    """Comprehensive tests for InvoicesModule"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.invoices = self.client.invoices

    @patch('baselinker.client.requests.Session.post')
    def test_get_invoices(self, mock_post):
        """Test get_invoices method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "invoices": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.invoices.get_invoices(
            date_from=1640995200,
            date_to=1641081600,
            id_from=1,
            id_to=100,
            series_id=1
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInvoices'

    @patch('baselinker.client.requests.Session.post')
    def test_add_invoice(self, mock_post):
        """Test add_invoice method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "invoice_id": 123}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.invoices.add_invoice(
            order_id=12345,
            series_id=1,
            vat_rate=23
        )
        
        assert result["invoice_id"] == 123
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addInvoice'

    def test_add_invoice_validation(self):
        """Test validation for add_invoice"""
        with pytest.raises(ValueError, match="Missing required parameters: order_id"):
            self.invoices.add_invoice()

    @patch('baselinker.client.requests.Session.post')
    def test_get_series(self, mock_post):
        """Test get_series method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "series": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.invoices.get_series()
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getSeries'

    @patch('baselinker.client.requests.Session.post')
    def test_set_order_payment(self, mock_post):
        """Test set_order_payment method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.invoices.set_order_payment(
            order_id=12345,
            payment_done=1,
            payment_date=1640995200
        )
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'setOrderPayment'

    def test_set_order_payment_validation(self):
        """Test validation for set_order_payment"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.invoices.set_order_payment()

    @patch('baselinker.client.requests.Session.post')
    def test_get_order_payments_history(self, mock_post):
        """Test get_order_payments_history method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "payments": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.invoices.get_order_payments_history(order_id=12345)
        
        assert result["status"] == "SUCCESS"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrderPaymentsHistory'

    def test_get_order_payments_history_validation(self):
        """Test validation for get_order_payments_history"""
        with pytest.raises(ValueError, match="Missing required parameters: order_id"):
            self.invoices.get_order_payments_history()

    @patch('baselinker.client.requests.Session.post')
    def test_get_invoice_file(self, mock_post):
        """Test get_invoice_file method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "file": "base64data"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.invoices.get_invoice_file(invoice_id=123)
        
        assert result["file"] == "base64data"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInvoiceFile'

    def test_get_invoice_file_validation(self):
        """Test validation for get_invoice_file"""
        with pytest.raises(ValueError, match="Missing required parameters: invoice_id"):
            self.invoices.get_invoice_file()

    @patch('baselinker.client.requests.Session.post')
    def test_get_receipt_file(self, mock_post):
        """Test get_receipt_file method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "file": "base64data"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.invoices.get_receipt_file(receipt_id=456)
        
        assert result["file"] == "base64data"
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getReceiptFile'

    def test_get_receipt_file_validation(self):
        """Test validation for get_receipt_file"""
        with pytest.raises(ValueError, match="Missing required parameters: receipt_id"):
            self.invoices.get_receipt_file()