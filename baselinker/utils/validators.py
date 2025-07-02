from typing import Dict, Any, List, Optional, Union


def validate_parameters(
    params: Dict[str, Any], 
    required: List[str] = None, 
    optional: Dict[str, type] = None
) -> None:
    """
    Validate API parameters
    
    Args:
        params: Parameters to validate
        required: List of required parameter names
        optional: Dict of optional parameters with their expected types
        
    Raises:
        ValueError: If validation fails
    """
    if required:
        missing = []
        for param in required:
            if param not in params or params[param] is None or (isinstance(params[param], str) and params[param].strip() == ""):
                missing.append(param)
        if missing:
            raise ValueError(f"Missing required parameters: {', '.join(missing)}")
    
    if optional:
        for param, expected_type in optional.items():
            if param in params and params[param] is not None and not isinstance(params[param], expected_type):
                raise ValueError(f"Invalid type for parameter {param}")


def validate_email(email: str) -> None:
    """Validate email format"""
    if not email or not isinstance(email, str):
        raise ValueError("Invalid email format")
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email format")


def validate_phone(phone: str) -> None:
    """Validate phone format"""
    if not phone or not isinstance(phone, str):
        raise ValueError("Invalid phone format")
    import re
    clean_phone = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    if len(clean_phone) < 4 or len(clean_phone) > 15:
        raise ValueError("Invalid phone format")
    pattern = r'^[\+]?[\d]+$'
    if not re.match(pattern, clean_phone):
        raise ValueError("Invalid phone format")


def validate_required_fields(data: Dict[str, Any], required_fields: List[str]) -> None:
    """Validate required fields are present"""
    missing = []
    for field in required_fields:
        if field not in data or data[field] is None or (isinstance(data[field], str) and data[field].strip() == ""):
            missing.append(field)
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")


def validate_currency(currency: str) -> bool:
    """Validate currency code"""
    valid_currencies = ['PLN', 'EUR', 'USD', 'GBP', 'CZK', 'SEK', 'DKK', 'NOK']
    return currency.upper() in valid_currencies


def validate_country_code(code: str) -> bool:
    """Validate ISO country code"""
    return len(code) == 2 and code.isalpha()