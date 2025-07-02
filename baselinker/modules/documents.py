from typing import Dict, Any
from .base import BaseModule
from ..utils.validators import validate_parameters


class DocumentsModule(BaseModule):
    """Warehouse documents management module"""
    
    # Warehouse Documents
    def get_inventory_documents(self, **kwargs) -> Dict[str, Any]:
        """Get warehouse documents"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryDocuments', kwargs)
    
    def get_inventory_document_items(self, **kwargs) -> Dict[str, Any]:
        """Get warehouse document items"""
        required = ['document_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryDocumentItems', kwargs)
    
    def get_inventory_document_series(self, **kwargs) -> Dict[str, Any]:
        """Get warehouse document series"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryDocumentSeries', kwargs)
    
    # Purchase Orders
    def get_inventory_purchase_orders(self, **kwargs) -> Dict[str, Any]:
        """Get warehouse purchase orders"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryPurchaseOrders', kwargs)
    
    def get_inventory_purchase_order_items(self, **kwargs) -> Dict[str, Any]:
        """Get warehouse purchase order items"""
        required = ['purchase_order_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryPurchaseOrderItems', kwargs)
    
    def get_inventory_purchase_order_series(self, **kwargs) -> Dict[str, Any]:
        """Get warehouse purchase order series"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryPurchaseOrderSeries', kwargs)