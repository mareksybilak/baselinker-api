from typing import Dict, Any
from .base import BaseModule
from ..utils.validators import validate_parameters


class ProductsModule(BaseModule):
    """Product catalog management module"""
    
    def get_inventories(self) -> Dict[str, Any]:
        """Get list of BaseLinker catalogs"""
        return self._make_request('getInventories')
    
    def add_inventory(self, **kwargs) -> Dict[str, Any]:
        """Create new BaseLinker catalog"""
        required = ['name']
        validate_parameters(kwargs, required)
        return self._make_request('addInventory', kwargs)
    
    def delete_inventory(self, **kwargs) -> Dict[str, Any]:
        """Delete BaseLinker catalog"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('deleteInventory', kwargs)
    
    def get_inventory_products_list(self, **kwargs) -> Dict[str, Any]:
        """Get products list from BaseLinker catalog"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryProductsList', kwargs)
    
    def get_inventory_products_data(self, **kwargs) -> Dict[str, Any]:
        """Get detailed products data from BaseLinker catalog"""
        required = ['inventory_id', 'products']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryProductsData', kwargs)
    
    def add_inventory_product(self, **kwargs) -> Dict[str, Any]:
        """Add or update product in BaseLinker catalog"""
        required = ['inventory_id', 'product_id']
        validate_parameters(kwargs, required)
        return self._make_request('addInventoryProduct', kwargs)
    
    def delete_inventory_product(self, **kwargs) -> Dict[str, Any]:
        """Delete product from BaseLinker catalog"""
        required = ['inventory_id', 'product_id']
        validate_parameters(kwargs, required)
        return self._make_request('deleteInventoryProduct', kwargs)
    
    def get_inventory_products_stock(self, **kwargs) -> Dict[str, Any]:
        """Get product stock levels from BaseLinker catalog"""
        required = ['inventory_id', 'products']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryProductsStock', kwargs)
    
    def update_inventory_products_stock(self, **kwargs) -> Dict[str, Any]:
        """Update product stock levels in BaseLinker catalog"""
        required = ['inventory_id', 'products']
        validate_parameters(kwargs, required)
        return self._make_request('updateInventoryProductsStock', kwargs)
    
    def get_inventory_products_prices(self, **kwargs) -> Dict[str, Any]:
        """Get product prices from BaseLinker catalog"""
        required = ['inventory_id', 'products']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryProductsPrices', kwargs)
    
    def update_inventory_products_prices(self, **kwargs) -> Dict[str, Any]:
        """Update product prices in BaseLinker catalog"""
        required = ['inventory_id', 'products']
        validate_parameters(kwargs, required)
        return self._make_request('updateInventoryProductsPrices', kwargs)
    
    def get_inventory_product_logs(self, **kwargs) -> Dict[str, Any]:
        """Get product change logs"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryProductLogs', kwargs)
    
    # Categories
    def get_inventory_categories(self, **kwargs) -> Dict[str, Any]:
        """Get categories from BaseLinker catalog"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryCategories', kwargs)
    
    def add_inventory_category(self, **kwargs) -> Dict[str, Any]:
        """Add category to BaseLinker catalog"""
        required = ['inventory_id', 'name']
        validate_parameters(kwargs, required)
        return self._make_request('addInventoryCategory', kwargs)
    
    def delete_inventory_category(self, **kwargs) -> Dict[str, Any]:
        """Delete category from BaseLinker catalog"""
        required = ['inventory_id', 'category_id']
        validate_parameters(kwargs, required)
        return self._make_request('deleteInventoryCategory', kwargs)
    
    # Tags
    def get_inventory_tags(self, **kwargs) -> Dict[str, Any]:
        """Get inventory tags"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryTags', kwargs)
    
    # Manufacturers
    def get_inventory_manufacturers(self, **kwargs) -> Dict[str, Any]:
        """Get manufacturers from BaseLinker catalog"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryManufacturers', kwargs)
    
    def add_inventory_manufacturer(self, **kwargs) -> Dict[str, Any]:
        """Add manufacturer to BaseLinker catalog"""
        required = ['inventory_id', 'name']
        validate_parameters(kwargs, required)
        return self._make_request('addInventoryManufacturer', kwargs)
    
    def delete_inventory_manufacturer(self, **kwargs) -> Dict[str, Any]:
        """Delete manufacturer from BaseLinker catalog"""
        required = ['inventory_id', 'manufacturer_id']
        validate_parameters(kwargs, required)
        return self._make_request('deleteInventoryManufacturer', kwargs)
    
    # Extra fields and integrations
    def get_inventory_extra_fields(self, **kwargs) -> Dict[str, Any]:
        """Get inventory extra fields configuration"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryExtraFields', kwargs)
    
    def get_inventory_integrations(self, **kwargs) -> Dict[str, Any]:
        """Get inventory integrations"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryIntegrations', kwargs)
    
    def get_inventory_available_text_field_keys(self, **kwargs) -> Dict[str, Any]:
        """Get available text field keys for inventory"""
        required = ['inventory_id']
        validate_parameters(kwargs, required)
        return self._make_request('getInventoryAvailableTextFieldKeys', kwargs)
    
    # Macro triggers
    def run_product_macro_trigger(self, **kwargs) -> Dict[str, Any]:
        """Run product macro trigger"""
        required = ['inventory_id', 'product_id', 'trigger_id']
        validate_parameters(kwargs, required)
        return self._make_request('runProductMacroTrigger', kwargs)