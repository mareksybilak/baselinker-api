from typing import Dict, Any
from .base import BaseModule
from ..utils.validators import validate_parameters


class InventoryModule(BaseModule):
    """Inventory and warehouse management module"""
    
    # Warehouses
    def get_inventory_warehouses(self, **kwargs) -> Dict[str, Any]:
        """Get warehouses from BaseLinker catalog"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryWarehouses', kwargs)
    
    def add_inventory_warehouse(self, **kwargs) -> Dict[str, Any]:
        """Add warehouse to BaseLinker catalog"""
        required = ['inventory_id', 'warehouse_id', 'name']
        validate_parameters(kwargs, required)
        return self._make_request('addInventoryWarehouse', kwargs)
    
    def delete_inventory_warehouse(self, **kwargs) -> Dict[str, Any]:
        """Delete warehouse from BaseLinker catalog"""
        required = ['inventory_id', 'warehouse_id']
        validate_parameters(kwargs, required)
        return self._make_request('deleteInventoryWarehouse', kwargs)
    
    # Price Groups
    def get_inventory_price_groups(self, **kwargs) -> Dict[str, Any]:
        """Get price groups from BaseLinker catalog"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryPriceGroups', kwargs)
    
    def add_inventory_price_group(self, **kwargs) -> Dict[str, Any]:
        """Add price group to BaseLinker catalog"""
        required = ['inventory_id', 'price_group_id', 'name']
        validate_parameters(kwargs, required)
        return self._make_request('addInventoryPriceGroup', kwargs)
    
    def delete_inventory_price_group(self, **kwargs) -> Dict[str, Any]:
        """Delete price group from BaseLinker catalog"""
        required = ['inventory_id', 'price_group_id']
        validate_parameters(kwargs, required)
        return self._make_request('deleteInventoryPriceGroup', kwargs)