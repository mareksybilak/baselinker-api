from typing import Dict, Any
from .base import BaseModule
from ..utils.validators import validate_parameters


class ReturnsModule(BaseModule):
    """Order returns management module"""
    
    def add_order_return(self, **kwargs) -> Dict[str, Any]:
        """Add new order return"""
        required = ['order_id', 'return_status', 'products']
        validate_parameters(kwargs, required)
        return self._make_request('addOrderReturn', kwargs)
    
    def get_order_returns(self, **kwargs) -> Dict[str, Any]:
        """Get order returns from specific date"""
        return self._make_request('getOrderReturns', kwargs)
    
    def set_order_return_fields(self, **kwargs) -> Dict[str, Any]:
        """Update order return fields"""
        required = ['return_id']
        validate_parameters(kwargs, required)
        return self._make_request('setOrderReturnFields', kwargs)
    
    def set_order_return_status(self, **kwargs) -> Dict[str, Any]:
        """Update order return status"""
        required = ['return_id', 'return_status']
        validate_parameters(kwargs, required)
        return self._make_request('setOrderReturnStatus', kwargs)
    
    def get_order_return_journal_list(self, **kwargs) -> Dict[str, Any]:
        """Get order returns journal list"""
        return self._make_request('getOrderReturnJournalList', kwargs)
    
    def get_order_return_extra_fields(self) -> Dict[str, Any]:
        """Get order return extra fields configuration"""
        return self._make_request('getOrderReturnExtraFields')
    
    def get_order_return_status_list(self) -> Dict[str, Any]:
        """Get list of order return statuses"""
        return self._make_request('getOrderReturnStatusList')
    
    def get_order_return_payments_history(self, **kwargs) -> Dict[str, Any]:
        """Get order return payments history"""
        required = ['return_id']
        validate_parameters(kwargs, required)
        return self._make_request('getOrderReturnPaymentsHistory', kwargs)
    
    def get_order_return_reasons_list(self) -> Dict[str, Any]:
        """Get list of order return reasons"""
        return self._make_request('getOrderReturnReasonsList')
    
    def get_order_return_product_statuses(self) -> Dict[str, Any]:
        """Get order return product statuses"""
        return self._make_request('getOrderReturnProductStatuses')