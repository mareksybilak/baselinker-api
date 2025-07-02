from typing import Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import BaseLinkerClient


class BaseModule:
    """Base class for all API modules"""
    
    def __init__(self, client: 'BaseLinkerClient'):
        self.client = client
    
    def _make_request(self, method: str, parameters: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make API request through the main client"""
        return self.client._make_request(method, parameters)