from typing import Dict, Any
from .base import BaseModule
from ..utils.validators import validate_parameters


class DevicesModule(BaseModule):
    """Devices and automation management module"""
    
    # Printers
    def register_printers(self, **kwargs) -> Dict[str, Any]:
        """Register printers"""
        required = ['printers']
        validate_parameters(kwargs, required)
        return self._make_request('registerPrinters', kwargs)
    
    def get_printers(self) -> Dict[str, Any]:
        """Get registered printers"""
        return self._make_request('getPrinters')
    
    def get_printer_jobs(self, **kwargs) -> Dict[str, Any]:
        """Get printer jobs"""
        return self._make_request('getPrinterJobs', kwargs)
    
    def set_printer_jobs_status(self, **kwargs) -> Dict[str, Any]:
        """Set printer jobs status"""
        required = ['jobs']
        validate_parameters(kwargs, required)
        return self._make_request('setPrinterJobsStatus', kwargs)
    
    def get_printer_receipts(self, **kwargs) -> Dict[str, Any]:
        """Get printer receipts"""
        return self._make_request('getPrinterReceipts', kwargs)
    
    def set_printer_receipts_status(self, **kwargs) -> Dict[str, Any]:
        """Set printer receipts status"""
        required = ['receipts']
        validate_parameters(kwargs, required)
        return self._make_request('setPrinterReceiptsStatus', kwargs)
    
    def add_printer_receipt_file(self, **kwargs) -> Dict[str, Any]:
        """Add printer receipt file"""
        required = ['receipt_id', 'file']
        validate_parameters(kwargs, required)
        return self._make_request('addPrinterReceiptFile', kwargs)
    
    # Scales
    def register_scales(self, **kwargs) -> Dict[str, Any]:
        """Register scales"""
        required = ['scales']
        validate_parameters(kwargs, required)
        return self._make_request('registerScales', kwargs)
    
    def add_scale_weight(self, **kwargs) -> Dict[str, Any]:
        """Add scale weight measurement"""
        required = ['scale_id', 'weight']
        validate_parameters(kwargs, required)
        return self._make_request('addScaleWeight', kwargs)
    
    # Logging and automation
    def add_log(self, **kwargs) -> Dict[str, Any]:
        """Add log entry"""
        required = ['message']
        validate_parameters(kwargs, required)
        return self._make_request('addLog', kwargs)
    
    def add_automatic_action(self, **kwargs) -> Dict[str, Any]:
        """Add automatic action"""
        required = ['action_type', 'conditions', 'actions']
        validate_parameters(kwargs, required)
        return self._make_request('addAutomaticAction', kwargs)
    
    def unsubscribe_webhook(self, **kwargs) -> Dict[str, Any]:
        """Unsubscribe webhook"""
        required = ['webhook_id']
        validate_parameters(kwargs, required)
        return self._make_request('unsubscribeWebhook', kwargs)
    
    def enable_module(self, **kwargs) -> Dict[str, Any]:
        """Enable module"""
        required = ['module_id']
        validate_parameters(kwargs, required)
        return self._make_request('enableModule', kwargs)
    
    # ERP and Connect
    def get_erp_jobs(self, **kwargs) -> Dict[str, Any]:
        """Get ERP jobs"""
        return self._make_request('getErpJobs', kwargs)
    
    def get_connect_integrations(self) -> Dict[str, Any]:
        """Get Connect integrations"""
        return self._make_request('getConnectIntegrations')
    
    def get_connect_integration_contractors(self, **kwargs) -> Dict[str, Any]:
        """Get Connect integration contractors"""
        required = ['integration_id']
        validate_parameters(kwargs, required)
        return self._make_request('getConnectIntegrationContractors', kwargs)
    
    def get_connect_contractor_credit_history(self, **kwargs) -> Dict[str, Any]:
        """Get Connect contractor credit history"""
        required = ['contractor_id']
        validate_parameters(kwargs, required)
        return self._make_request('getConnectContractorCreditHistory', kwargs)
    
    def add_connect_contractor_credit(self, **kwargs) -> Dict[str, Any]:
        """Add Connect contractor credit"""
        required = ['contractor_id', 'amount']
        validate_parameters(kwargs, required)
        return self._make_request('addConnectContractorCredit', kwargs)