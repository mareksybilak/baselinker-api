class BaseLinkerError(Exception):
    """Base exception for BaseLinker API errors"""
    pass


class AuthenticationError(BaseLinkerError):
    """Raised when API token is invalid or missing"""
    pass


class RateLimitError(BaseLinkerError):
    """Raised when API rate limit is exceeded"""
    pass


class ValidationError(BaseLinkerError):
    """Raised when request parameters are invalid"""
    pass


class APIError(BaseLinkerError):
    """Raised when API returns an error response"""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code