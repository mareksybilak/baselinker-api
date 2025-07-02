import pytest
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient
from baselinker.modules import (
    OrdersModule, ProductsModule, InventoryModule, CourierModule,
    ExternalStorageModule, ReturnsModule, InvoicesModule, 
    DocumentsModule, DevicesModule
)


class TestModularStructure:
    """Test the modular structure of BaseLinkerClient"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
    
    def test_client_has_all_modules(self):
        """Test that client has all required modules"""
        assert isinstance(self.client.orders, OrdersModule)
        assert isinstance(self.client.products, ProductsModule)
        assert isinstance(self.client.inventory, InventoryModule)
        assert isinstance(self.client.courier, CourierModule)
        assert isinstance(self.client.external_storage, ExternalStorageModule)
        assert isinstance(self.client.returns, ReturnsModule)
        assert isinstance(self.client.invoices, InvoicesModule)
        assert isinstance(self.client.documents, DocumentsModule)
        assert isinstance(self.client.devices, DevicesModule)
    
    def test_modules_have_client_reference(self):
        """Test that modules have reference to the main client"""
        assert self.client.orders.client is self.client
        assert self.client.products.client is self.client
        assert self.client.inventory.client is self.client
        assert self.client.courier.client is self.client
        assert self.client.external_storage.client is self.client
        assert self.client.returns.client is self.client
        assert self.client.invoices.client is self.client
        assert self.client.documents.client is self.client
        assert self.client.devices.client is self.client
    
    @patch('baselinker.client.requests.Session.post')
    def test_module_requests_use_main_client(self, mock_post):
        """Test that module requests go through main client"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "orders": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Call through module
        self.client.orders.get_orders()
        
        # Verify request was made through main client
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrders'
    
    def test_purely_modular_access(self):
        """Test that client is purely modular - no direct methods"""
        # Client should not have old direct methods
        assert not hasattr(self.client, 'get_orders')
        assert not hasattr(self.client, 'add_order')
        assert not hasattr(self.client, 'get_inventories')
        
        # But should have all modules
        assert hasattr(self.client, 'orders')
        assert hasattr(self.client, 'products')
        assert hasattr(self.client, 'inventory')


class TestOrdersModule:
    """Test OrdersModule functionality"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.orders = self.client.orders
    
    @patch('baselinker.client.requests.Session.post')
    def test_get_orders_by_email(self, mock_post):
        """Test get_orders_by_email method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "orders": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_orders_by_email(email="test@example.com")
        
        assert result == {"status": "SUCCESS", "orders": []}
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrdersByEmail'
    
    @patch('baselinker.client.requests.Session.post')
    def test_get_orders_by_phone(self, mock_post):
        """Test get_orders_by_phone method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "orders": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.orders.get_orders_by_phone(phone="+48123456789")
        
        assert result == {"status": "SUCCESS", "orders": []}
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getOrdersByPhone'
    
    def test_get_orders_by_email_validation(self):
        """Test validation for get_orders_by_email"""
        with pytest.raises(ValueError, match="Missing required parameters: email"):
            self.orders.get_orders_by_email()


class TestProductsModule:
    """Test ProductsModule functionality"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.products = self.client.products
    
    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_manufacturers(self, mock_post):
        """Test get_inventory_manufacturers method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "manufacturers": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_manufacturers(inventory_id=123)
        
        assert result == {"status": "SUCCESS", "manufacturers": []}
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryManufacturers'
    
    @patch('baselinker.client.requests.Session.post')
    def test_get_inventory_tags(self, mock_post):
        """Test get_inventory_tags method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "tags": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.products.get_inventory_tags(inventory_id=123)
        
        assert result == {"status": "SUCCESS", "tags": []}
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInventoryTags'


class TestInvoicesModule:
    """Test InvoicesModule functionality"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.invoices = self.client.invoices
    
    @patch('baselinker.client.requests.Session.post')
    def test_add_invoice(self, mock_post):
        """Test add_invoice method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "invoice_id": 123}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.invoices.add_invoice(order_id=456)
        
        assert result == {"status": "SUCCESS", "invoice_id": 123}
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'addInvoice'
    
    @patch('baselinker.client.requests.Session.post')
    def test_get_invoices(self, mock_post):
        """Test get_invoices method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "invoices": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.invoices.get_invoices()
        
        assert result == {"status": "SUCCESS", "invoices": []}
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getInvoices'


class TestCourierModule:
    """Test CourierModule functionality"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
        self.courier = self.client.courier
    
    @patch('baselinker.client.requests.Session.post')
    def test_get_courier_services(self, mock_post):
        """Test get_courier_services method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "services": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_courier_services(courier_code="dpd")
        
        assert result == {"status": "SUCCESS", "services": []}
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getCourierServices'
    
    @patch('baselinker.client.requests.Session.post')
    def test_get_courier_fields(self, mock_post):
        """Test get_courier_fields method"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS", "fields": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        result = self.courier.get_courier_fields(courier_code="dpd")
        
        assert result == {"status": "SUCCESS", "fields": []}
        call_args = mock_post.call_args
        assert call_args[1]['data']['method'] == 'getCourierFields'


class TestValidators:
    """Test parameter validation"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")
    
    def test_missing_required_parameters(self):
        """Test validation of missing required parameters"""
        with pytest.raises(ValueError, match="Missing required parameters"):
            self.client.orders.add_order()  # Missing required params
    
    def test_valid_required_parameters(self):
        """Test that validation passes with required parameters"""
        with patch('baselinker.client.requests.Session.post') as mock_post:
            mock_response = Mock()
            mock_response.json.return_value = {"status": "SUCCESS", "order_id": 123}
            mock_response.raise_for_status.return_value = None
            mock_post.return_value = mock_response
            
            # Should not raise validation error
            result = self.client.orders.add_order(
                order_source_id=1,
                date_add=1640995200,
                order_status_id=1
            )
            
            assert result == {"status": "SUCCESS", "order_id": 123}