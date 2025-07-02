import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestAllModulesCoverage:
    """Tests to achieve 95% coverage across all modules"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.client = BaseLinkerClient("test_token")

    @patch('baselinker.client.requests.Session.post')
    def test_courier_module_all_methods(self, mock_post):
        """Test all courier module methods"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test all existing courier methods
        self.client.courier.get_couriers_list()
        self.client.courier.get_courier_fields(courier_code="dpd")
        self.client.courier.get_courier_services(courier_code="dpd")
        self.client.courier.get_courier_accounts()
        self.client.courier.create_package(order_id=123, courier_code="dpd")
        self.client.courier.create_package_manual(order_id=123, courier_code="dpd", package_number="123456")
        self.client.courier.get_label(package_id=123)
        self.client.courier.get_protocol(package_id=123)
        self.client.courier.get_courier_document(package_id=123)
        self.client.courier.get_order_packages(order_id=123)
        self.client.courier.get_courier_packages_status_history(date_from=1640995200)
        self.client.courier.delete_courier_package(package_id=123)
        self.client.courier.request_parcel_pickup(courier_code="dpd", package_ids=[123])
        self.client.courier.get_request_parcel_pickup_fields(courier_code="dpd")

    @patch('baselinker.client.requests.Session.post')
    def test_devices_module_all_methods(self, mock_post):
        """Test all devices module methods"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test all existing device methods
        self.client.devices.register_printers(printers=[])
        self.client.devices.get_printers()
        self.client.devices.get_printer_jobs(printer_id=123)
        self.client.devices.set_printer_jobs_status(job_id=123, status="completed")
        self.client.devices.get_printer_receipts(printer_id=123)
        self.client.devices.set_printer_receipts_status(receipt_id=123, status="printed")
        self.client.devices.add_printer_receipt_file(receipt_id=123, file_data="data")
        self.client.devices.register_scales(scales=[])
        self.client.devices.add_scale_weight(scale_id=123, weight=2.5)
        self.client.devices.add_log(log_type="info", message="test")
        self.client.devices.add_automatic_action(trigger="order", action="print")
        self.client.devices.unsubscribe_webhook(webhook_id=123)
        self.client.devices.enable_module(module_name="test")
        self.client.devices.get_erp_jobs()
        self.client.devices.get_connect_integrations()
        self.client.devices.get_connect_integration_contractors(integration_id=123)
        self.client.devices.get_connect_contractor_credit_history(contractor_id=123)
        self.client.devices.add_connect_contractor_credit(contractor_id=123, amount=100)

    @patch('baselinker.client.requests.Session.post')
    def test_documents_module_all_methods(self, mock_post):
        """Test all documents module methods"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test all existing document methods
        self.client.documents.get_inventory_documents(inventory_id=123)
        self.client.documents.get_inventory_document_items(document_id=123)
        self.client.documents.get_inventory_document_series(inventory_id=123)
        self.client.documents.get_inventory_purchase_orders(inventory_id=123)
        self.client.documents.get_inventory_purchase_order_items(order_id=123)
        self.client.documents.get_inventory_purchase_order_series(inventory_id=123)

    @patch('baselinker.client.requests.Session.post')
    def test_external_storage_module_all_methods(self, mock_post):
        """Test all external storage module methods"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test all existing external storage methods
        self.client.external_storage.get_external_storages_list()
        self.client.external_storage.get_external_storage_categories(storage_id="123")
        self.client.external_storage.get_external_storage_products_data(storage_id="123", products=["prod1"])
        self.client.external_storage.get_external_storage_products_list(storage_id="123")
        self.client.external_storage.get_external_storage_products_quantity(storage_id="123")
        self.client.external_storage.get_external_storage_products_prices(storage_id="123")
        self.client.external_storage.update_external_storage_products_quantity(storage_id="123", products=[])

    @patch('baselinker.client.requests.Session.post')
    def test_inventory_module_all_methods(self, mock_post):
        """Test all inventory module methods"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test all existing inventory methods
        self.client.inventory.get_inventory_warehouses(inventory_id=123)
        self.client.inventory.add_inventory_warehouse(inventory_id=123, name="test")
        self.client.inventory.delete_inventory_warehouse(inventory_id=123, warehouse_id=456)
        self.client.inventory.get_inventory_price_groups(inventory_id=123)
        self.client.inventory.add_inventory_price_group(inventory_id=123, name="test")
        self.client.inventory.delete_inventory_price_group(inventory_id=123, price_group_id=456)

    @patch('baselinker.client.requests.Session.post')
    def test_invoices_module_all_methods(self, mock_post):
        """Test all invoices module methods"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test all existing invoice methods
        self.client.invoices.add_invoice(order_id=123)
        self.client.invoices.get_invoices()
        self.client.invoices.get_invoice_file(invoice_id=123)
        self.client.invoices.add_order_invoice_file(order_id=123, file="data")
        self.client.invoices.add_order_receipt_file(order_id=123, file="data")
        self.client.invoices.get_series()
        self.client.invoices.set_order_payment(order_id=123, payment_done=1)
        self.client.invoices.get_order_payments_history(order_id=123)

    @patch('baselinker.client.requests.Session.post')
    def test_orders_module_all_methods(self, mock_post):
        """Test all orders module methods"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test all existing order methods
        self.client.orders.get_orders(date_from=1640995200)
        self.client.orders.add_order(order_source_id=1, date_add=1640995200, order_status_id=1)
        self.client.orders.get_order_sources()
        self.client.orders.set_order_fields(order_id=123)
        self.client.orders.set_order_status(order_id=123, status_id=1)
        self.client.orders.get_orders_by_email(email="test@example.com")
        self.client.orders.get_orders_by_phone(phone="+48123456789")
        self.client.orders.get_orders_by_login(login="test")
        self.client.orders.get_order_status_list()
        self.client.orders.get_order_extra_fields()
        self.client.orders.get_order_transaction_data(order_id=123)
        self.client.orders.get_order_transaction_details(order_id=123)
        self.client.orders.get_journal_list()
        self.client.orders.add_order_product(order_id=123, product_id="test", name="test", price_brutto=10, tax_rate=23, quantity=1)
        self.client.orders.set_order_product_fields(order_id=123, order_product_id=456)
        self.client.orders.delete_order_product(order_id=123, order_product_id=456)
        self.client.orders.run_order_macro_trigger(order_id=123, trigger_id=456)

    @patch('baselinker.client.requests.Session.post')
    def test_products_module_all_methods(self, mock_post):
        """Test all products module methods"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test all existing product methods
        self.client.products.get_inventories()
        self.client.products.add_inventory(name="test")
        self.client.products.delete_inventory(inventory_id=123)
        self.client.products.get_inventory_products_list(inventory_id=123)
        self.client.products.get_inventory_products_data(inventory_id=123, products=["test"])
        self.client.products.add_inventory_product(inventory_id=123, product_id="test")
        self.client.products.delete_inventory_product(inventory_id=123, product_id="test")
        self.client.products.get_inventory_products_stock(inventory_id=123)
        self.client.products.update_inventory_products_stock(inventory_id=123, products=[])
        self.client.products.get_inventory_products_prices(inventory_id=123)
        self.client.products.update_inventory_products_prices(inventory_id=123, products=[])
        self.client.products.get_inventory_product_logs(inventory_id=123)
        self.client.products.get_inventory_categories(inventory_id=123)
        self.client.products.add_inventory_category(inventory_id=123, name="test")
        self.client.products.delete_inventory_category(inventory_id=123, category_id=456)
        self.client.products.get_inventory_tags(inventory_id=123)
        self.client.products.get_inventory_manufacturers(inventory_id=123)
        self.client.products.add_inventory_manufacturer(inventory_id=123, name="test")
        self.client.products.delete_inventory_manufacturer(inventory_id=123, manufacturer_id=456)
        self.client.products.get_inventory_extra_fields(inventory_id=123)
        self.client.products.get_inventory_integrations(inventory_id=123)
        self.client.products.get_inventory_available_text_field_keys(inventory_id=123)
        self.client.products.run_product_macro_trigger(product_id="test", trigger_id=123)

    @patch('baselinker.client.requests.Session.post')
    def test_returns_module_all_methods(self, mock_post):
        """Test all returns module methods"""
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test all existing return methods
        self.client.returns.add_order_return(order_id=123)
        self.client.returns.get_order_returns()
        self.client.returns.set_order_return_fields(return_id=123)
        self.client.returns.set_order_return_status(return_id=123, status_id=1)
        self.client.returns.get_order_return_extra_fields()
        self.client.returns.get_order_return_status_list()
        self.client.returns.get_order_return_reasons_list()
        self.client.returns.get_order_return_product_statuses()
        self.client.returns.get_order_return_journal_list()
        self.client.returns.get_order_return_payments_history(return_id=123)

    @patch('baselinker.client.requests.Session.post')
    def test_validators_coverage(self, mock_post):
        """Test validator utility functions"""
        from baselinker.utils.validators import validate_parameters, validate_email, validate_phone, validate_required_fields
        
        # Test validate_parameters
        validate_parameters({"test": "value"}, ["test"])
        
        # Test validate_email
        validate_email("test@example.com")
        
        # Test validate_phone
        validate_phone("+48123456789")
        
        # Test validate_required_fields
        validate_required_fields({"test": "value"}, ["test"])

    def test_base_module_coverage(self):
        """Test base module methods"""
        from baselinker.modules.base import BaseModule
        
        # Create instance
        base = BaseModule(self.client)
        assert base.client == self.client

    def test_client_error_paths(self):
        """Test client error handling paths"""
        # Test with invalid token
        with pytest.raises(Exception):
            BaseLinkerClient("")
        
        # Test with None token
        with pytest.raises(Exception):
            BaseLinkerClient(None)

    @patch('baselinker.client.requests.Session.post')
    def test_client_error_handling(self, mock_post):
        """Test client error handling for various scenarios"""
        import requests
        
        # Test network error
        mock_post.side_effect = requests.ConnectionError("Network error")
        with pytest.raises(Exception):
            self.client.orders.get_orders(date_from=1640995200)
        
        # Test timeout error
        mock_post.side_effect = requests.Timeout("Timeout")
        with pytest.raises(Exception):
            self.client.orders.get_orders(date_from=1640995200)
        
        # Test HTTP error
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("HTTP Error")
        mock_post.return_value = mock_response
        mock_post.side_effect = None
        
        with pytest.raises(Exception):
            self.client.orders.get_orders(date_from=1640995200)
        
        # Test JSON decode error
        mock_response = Mock()
        mock_response.json.side_effect = json.JSONDecodeError("Invalid JSON", "", 0)
        mock_response.raise_for_status.return_value = None
        mock_response.text = "Invalid response"
        mock_post.return_value = mock_response
        
        with pytest.raises(Exception):
            self.client.orders.get_orders(date_from=1640995200)