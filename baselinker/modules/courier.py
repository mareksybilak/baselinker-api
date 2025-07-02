from typing import Dict, Any
from .base import BaseModule
from ..utils.validators import validate_parameters


class CourierModule(BaseModule):
    """Courier and shipping management module"""
    
    def get_couriers_list(self) -> Dict[str, Any]:
        """Get list of available couriers"""
        return self._make_request('getCouriersList')
    
    def get_courier_fields(self, **kwargs) -> Dict[str, Any]:
        """Get courier form fields"""
        required = ['courier_code']
        validate_parameters(kwargs, required)
        return self._make_request('getCourierFields', kwargs)
    
    def get_courier_services(self, **kwargs) -> Dict[str, Any]:
        """Get courier services"""
        required = ['courier_code']
        validate_parameters(kwargs, required)
        return self._make_request('getCourierServices', kwargs)
    
    def get_courier_accounts(self, **kwargs) -> Dict[str, Any]:
        """Get courier API accounts"""
        required = ['courier_code']
        validate_parameters(kwargs, required)
        return self._make_request('getCourierAccounts', kwargs)
    
    def create_package(self, **kwargs) -> Dict[str, Any]:
        """Create shipment package in courier system"""
        required = ['order_id', 'courier_code']
        validate_parameters(kwargs, required)
        return self._make_request('createPackage', kwargs)
    
    def create_package_manual(self, **kwargs) -> Dict[str, Any]:
        """Manually create package with tracking number"""
        required = ['order_id', 'courier_code', 'package_number']
        validate_parameters(kwargs, required)
        return self._make_request('createPackageManual', kwargs)
    
    def get_label(self, **kwargs) -> Dict[str, Any]:
        """Download shipping label"""
        required = ['package_id']
        validate_parameters(kwargs, required)
        return self._make_request('getLabel', kwargs)
    
    def get_protocol(self, **kwargs) -> Dict[str, Any]:
        """Get shipping protocol"""
        required = ['package_id']
        validate_parameters(kwargs, required)
        return self._make_request('getProtocol', kwargs)
    
    def get_courier_document(self, **kwargs) -> Dict[str, Any]:
        """Get courier document"""
        required = ['document_id']
        validate_parameters(kwargs, required)
        return self._make_request('getCourierDocument', kwargs)
    
    def get_order_packages(self, **kwargs) -> Dict[str, Any]:
        """Get packages for specific order"""
        required = ['order_id']
        validate_parameters(kwargs, required)
        return self._make_request('getOrderPackages', kwargs)
    
    def get_courier_packages_status_history(self, **kwargs) -> Dict[str, Any]:
        """Get courier packages status history"""
        return self._make_request('getCourierPackagesStatusHistory', kwargs)
    
    def delete_courier_package(self, **kwargs) -> Dict[str, Any]:
        """Delete courier package"""
        required = ['package_id']
        validate_parameters(kwargs, required)
        return self._make_request('deleteCourierPackage', kwargs)
    
    def request_parcel_pickup(self, **kwargs) -> Dict[str, Any]:
        """Request parcel pickup from courier"""
        required = ['courier_code', 'package_ids', 'pickup_date']
        validate_parameters(kwargs, required)
        return self._make_request('requestParcelPickup', kwargs)
    
    def get_request_parcel_pickup_fields(self, **kwargs) -> Dict[str, Any]:
        """Get fields required for parcel pickup request"""
        required = ['courier_code']
        validate_parameters(kwargs, required)
        return self._make_request('getRequestParcelPickupFields', kwargs)