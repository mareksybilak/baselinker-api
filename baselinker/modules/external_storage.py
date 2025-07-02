from typing import Dict, Any
from .base import BaseModule
from ..utils.validators import validate_parameters


class ExternalStorageModule(BaseModule):
    """External storage management module"""
    
    def get_external_storages_list(self) -> Dict[str, Any]:
        """Get list of external storage connections"""
        return self._make_request('getExternalStoragesList')
    
    def get_external_storage_categories(self, **kwargs) -> Dict[str, Any]:
        """Get categories from external storage"""
        required = ['storage_id']
        validate_parameters(kwargs, required)
        return self._make_request('getExternalStorageCategories', kwargs)
    
    def get_external_storage_products_data(self, **kwargs) -> Dict[str, Any]:
        """Get detailed product data from external storage"""
        required = ['storage_id', 'products']
        validate_parameters(kwargs, required)
        return self._make_request('getExternalStorageProductsData', kwargs)
    
    def get_external_storage_products_list(self, **kwargs) -> Dict[str, Any]:
        """Get products list from external storage"""
        required = ['storage_id']
        validate_parameters(kwargs, required)
        return self._make_request('getExternalStorageProductsList', kwargs)
    
    def get_external_storage_products_quantity(self, **kwargs) -> Dict[str, Any]:
        """Get product stock quantities from external storage"""
        required = ['storage_id', 'products']
        validate_parameters(kwargs, required)
        return self._make_request('getExternalStorageProductsQuantity', kwargs)
    
    def get_external_storage_products_prices(self, **kwargs) -> Dict[str, Any]:
        """Get product prices from external storage"""
        required = ['storage_id', 'products']
        validate_parameters(kwargs, required)
        return self._make_request('getExternalStorageProductsPrices', kwargs)
    
    def update_external_storage_products_quantity(self, **kwargs) -> Dict[str, Any]:
        """Update product stock quantities in external storage"""
        required = ['storage_id', 'products']
        validate_parameters(kwargs, required)
        return self._make_request('updateExternalStorageProductsQuantity', kwargs)