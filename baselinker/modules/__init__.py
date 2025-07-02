from .orders import OrdersModule
from .products import ProductsModule
from .inventory import InventoryModule
from .courier import CourierModule
from .external_storage import ExternalStorageModule
from .returns import ReturnsModule
from .invoices import InvoicesModule
from .documents import DocumentsModule
from .devices import DevicesModule

__all__ = [
    "OrdersModule",
    "ProductsModule", 
    "InventoryModule",
    "CourierModule",
    "ExternalStorageModule",
    "ReturnsModule",
    "InvoicesModule",
    "DocumentsModule",
    "DevicesModule"
]