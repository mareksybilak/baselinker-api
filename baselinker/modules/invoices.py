from typing import Dict, Any
from .base import BaseModule
from ..utils.validators import validate_parameters


class InvoicesModule(BaseModule):
    """Invoices and payments management module"""
    
    # Invoices
    def add_invoice(self, **kwargs) -> Dict[str, Any]:
        """Create new invoice"""
        required = ['order_id']
        validate_parameters(kwargs, required)
        return self._make_request('addInvoice', kwargs)
    
    def get_invoices(self, **kwargs) -> Dict[str, Any]:
        """Get invoices list"""
        return self._make_request('getInvoices', kwargs)
    
    def get_invoice_file(self, **kwargs) -> Dict[str, Any]:
        """Get invoice file"""
        required = ['invoice_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInvoiceFile', kwargs)
    
    def add_order_invoice_file(self, **kwargs) -> Dict[str, Any]:
        """Add invoice file to order"""
        required = ['order_id', 'file']
        validate_parameters(kwargs, required)
        return self._make_request('addOrderInvoiceFile', kwargs)
    
    def add_order_receipt_file(self, **kwargs) -> Dict[str, Any]:
        """Add receipt file to order"""
        required = ['order_id', 'file']
        validate_parameters(kwargs, required)
        return self._make_request('addOrderReceiptFile', kwargs)
    
    # Document series
    def get_series(self, **kwargs) -> Dict[str, Any]:
        """Get document series (numerations)"""
        return self._make_request('getSeries', kwargs)
    
    # Payments
    def set_order_payment(self, **kwargs) -> Dict[str, Any]:
        """Set order payment status"""
        required = ['order_id']
        validate_parameters(kwargs, required)
        return self._make_request('setOrderPayment', kwargs)
    
    def get_order_payments_history(self, **kwargs) -> Dict[str, Any]:
        """Get order payments history"""
        required = ['order_id']
        validate_parameters(kwargs, required)
        return self._make_request('getOrderPaymentsHistory', kwargs)