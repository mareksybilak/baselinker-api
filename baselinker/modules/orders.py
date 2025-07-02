from typing import Dict, Any
from .base import BaseModule
from ..utils.validators import validate_parameters


class OrdersModule(BaseModule):
    """Orders management module"""
    
    def get_orders(self, **kwargs) -> Dict[str, Any]:
        """Download orders from BaseLinker order manager"""
        return self._make_request('getOrders', kwargs)
    
    def add_order(self, **kwargs) -> Dict[str, Any]:
        """Add new order to BaseLinker order manager"""
        required = ['order_source_id', 'date_add', 'order_status_id']
        validate_parameters(kwargs, required)
        return self._make_request('addOrder', kwargs)
    
    def get_order_sources(self) -> Dict[str, Any]:
        """Get list of order sources"""
        return self._make_request('getOrderSources')
    
    def set_order_fields(self, **kwargs) -> Dict[str, Any]:
        """Edit specific fields of an existing order"""
        required = ['order_id']
        validate_parameters(kwargs, required)
        return self._make_request('setOrderFields', kwargs)
    
    def set_order_status(self, **kwargs) -> Dict[str, Any]:
        """Change order status"""
        required = ['order_id', 'status_id']
        validate_parameters(kwargs, required)
        return self._make_request('setOrderStatus', kwargs)
    
    def get_orders_by_email(self, **kwargs) -> Dict[str, Any]:
        """Search orders by customer email"""
        required = ['email']
        validate_parameters(kwargs, required)
        return self._make_request('getOrdersByEmail', kwargs)
    
    def get_orders_by_phone(self, **kwargs) -> Dict[str, Any]:
        """Search orders by customer phone"""
        required = ['phone']
        validate_parameters(kwargs, required)
        return self._make_request('getOrdersByPhone', kwargs)
    
    def get_orders_by_login(self, **kwargs) -> Dict[str, Any]:
        """Search orders by customer login"""
        required = ['login']
        validate_parameters(kwargs, required)
        return self._make_request('getOrdersByLogin', kwargs)
    
    def get_order_status_list(self) -> Dict[str, Any]:
        """Get list of order statuses"""
        return self._make_request('getOrderStatusList')
    
    def get_order_extra_fields(self) -> Dict[str, Any]:
        """Get order extra fields configuration"""
        return self._make_request('getOrderExtraFields')
    
    def get_order_transaction_data(self, **kwargs) -> Dict[str, Any]:
        """Get order transaction data"""
        required = ['order_id']
        validate_parameters(kwargs, required)
        return self._make_request('getOrderTransactionData', kwargs)
    
    def get_order_transaction_details(self, **kwargs) -> Dict[str, Any]:
        """Get detailed order transaction data"""
        required = ['order_id']
        validate_parameters(kwargs, required)
        return self._make_request('getOrderTransactionDetails', kwargs)
    
    def get_journal_list(self, **kwargs) -> Dict[str, Any]:
        """Get journal/log entries for orders"""
        return self._make_request('getJournalList', kwargs)
    
    # Order Products
    def add_order_product(self, **kwargs) -> Dict[str, Any]:
        """Add product to existing order"""
        required = ['order_id', 'product_id', 'name', 'price_brutto', 'tax_rate', 'quantity']
        validate_parameters(kwargs, required)
        return self._make_request('addOrderProduct', kwargs)
    
    def set_order_product_fields(self, **kwargs) -> Dict[str, Any]:
        """Update order product fields"""
        required = ['order_id', 'order_product_id']
        validate_parameters(kwargs, required)
        return self._make_request('setOrderProductFields', kwargs)
    
    def delete_order_product(self, **kwargs) -> Dict[str, Any]:
        """Delete product from order"""
        required = ['order_id', 'order_product_id']
        validate_parameters(kwargs, required)
        return self._make_request('deleteOrderProduct', kwargs)
    
    # Macro triggers
    def run_order_macro_trigger(self, **kwargs) -> Dict[str, Any]:
        """Run order macro trigger"""
        required = ['order_id', 'trigger_id']
        validate_parameters(kwargs, required)
        return self._make_request('runOrderMacroTrigger', kwargs)