import pytest
from baselinker.utils.validators import (
    validate_parameters, validate_email, validate_phone, 
    validate_required_fields, validate_currency, validate_country_code
)


class TestValidatorsSimple:
    """Simple tests for validator utilities to achieve coverage"""

    def test_validate_parameters_basic(self):
        """Test basic parameter validation"""
        # Valid case
        validate_parameters({"test": "value"}, ["test"])
        
        # Missing required
        with pytest.raises(ValueError):
            validate_parameters({}, ["required"])
            
        # None value treated as missing
        with pytest.raises(ValueError):
            validate_parameters({"test": None}, ["test"])
            
        # Empty string treated as missing  
        with pytest.raises(ValueError):
            validate_parameters({"test": ""}, ["test"])
            
        # Whitespace treated as missing
        with pytest.raises(ValueError):
            validate_parameters({"test": "   "}, ["test"])

    def test_validate_parameters_types(self):
        """Test parameter type validation"""
        # Valid types
        validate_parameters(
            {"str_val": "test", "int_val": 123}, 
            [], 
            {"str_val": str, "int_val": int}
        )
        
        # Invalid type
        with pytest.raises(ValueError):
            validate_parameters(
                {"test": "string"}, 
                [], 
                {"test": int}
            )

    def test_validate_email_valid(self):
        """Test valid email validation"""
        validate_email("test@example.com")
        validate_email("user.name@domain.co.uk")

    def test_validate_email_invalid(self):
        """Test invalid email validation"""
        with pytest.raises(ValueError):
            validate_email("invalid")
            
        with pytest.raises(ValueError):
            validate_email("")
            
        with pytest.raises(ValueError):
            validate_email(None)

    def test_validate_phone_valid(self):
        """Test valid phone validation"""
        validate_phone("+48123456789")
        validate_phone("123456789")

    def test_validate_phone_invalid(self):
        """Test invalid phone validation"""
        with pytest.raises(ValueError):
            validate_phone("123")  # Too short
            
        with pytest.raises(ValueError):
            validate_phone("")
            
        with pytest.raises(ValueError):
            validate_phone(None)

    def test_validate_required_fields_basic(self):
        """Test required fields validation"""
        # Valid case
        validate_required_fields({"test": "value"}, ["test"])
        
        # Missing field
        with pytest.raises(ValueError):
            validate_required_fields({}, ["required"])

    def test_validate_currency(self):
        """Test currency validation"""
        assert validate_currency("PLN") == True
        assert validate_currency("EUR") == True
        assert validate_currency("USD") == True
        assert validate_currency("INVALID") == False

    def test_validate_country_code(self):
        """Test country code validation"""
        assert validate_country_code("PL") == True
        assert validate_country_code("US") == True
        assert validate_country_code("INVALID") == False
        assert validate_country_code("123") == False