import pytest
from baselinker.utils.validators import validate_parameters, validate_email, validate_phone, validate_required_fields


class TestValidatorsComprehensive:
    """Comprehensive tests for parameter validation utilities"""

    def test_validate_parameters_with_required_fields(self):
        """Test validate_parameters with required fields"""
        # Valid case
        params = {"field1": "value1", "field2": "value2"}
        required = ["field1", "field2"]
        
        # Should not raise exception
        validate_parameters(params, required)

    def test_validate_parameters_missing_required(self):
        """Test validate_parameters with missing required fields"""
        params = {"field1": "value1"}
        required = ["field1", "field2", "field3"]
        
        with pytest.raises(ValueError, match="Missing required parameters: field2, field3"):
            validate_parameters(params, required)

    def test_validate_parameters_with_optional_fields(self):
        """Test validate_parameters with optional field type checking"""
        params = {"field1": "value1", "field2": 123, "field3": True}
        required = ["field1"]
        optional = {"field2": int, "field3": bool, "field4": str}
        
        # Should not raise exception
        validate_parameters(params, required, optional)

    def test_validate_parameters_invalid_optional_type(self):
        """Test validate_parameters with invalid optional field types"""
        params = {"field1": "value1", "field2": "invalid"}
        required = ["field1"]
        optional = {"field2": int}
        
        with pytest.raises(ValueError, match="Invalid type for parameter field2"):
            validate_parameters(params, required, optional)

    def test_validate_parameters_empty_params(self):
        """Test validate_parameters with empty parameters"""
        params = {}
        required = ["field1"]
        
        with pytest.raises(ValueError, match="Missing required parameters: field1"):
            validate_parameters(params, required)

    def test_validate_parameters_no_requirements(self):
        """Test validate_parameters with no requirements"""
        params = {"field1": "value1"}
        
        # Should not raise exception
        validate_parameters(params)

    def test_validate_parameters_none_values(self):
        """Test validate_parameters with None values"""
        params = {"field1": None, "field2": "value2"}
        required = ["field1", "field2"]
        
        with pytest.raises(ValueError, match="Missing required parameters: field1"):
            validate_parameters(params, required)

    def test_validate_parameters_empty_string_values(self):
        """Test validate_parameters with empty string values"""
        params = {"field1": "", "field2": "value2"}
        required = ["field1", "field2"]
        
        with pytest.raises(ValueError, match="Missing required parameters: field1"):
            validate_parameters(params, required)

    def test_validate_email_valid(self):
        """Test validate_email with valid emails"""
        valid_emails = [
            "test@example.com",
            "user.name@domain.co.uk",
            "user+tag@example.org",
            "123@test.com"
        ]
        
        for email in valid_emails:
            # Should not raise exception
            validate_email(email)

    def test_validate_email_invalid(self):
        """Test validate_email with invalid emails"""
        invalid_emails = [
            "invalid-email",
            "@domain.com",
            "test@",
            "test..test@domain.com",
            "",
            None
        ]
        
        for email in invalid_emails:
            with pytest.raises(ValueError, match="Invalid email format"):
                validate_email(email)

    def test_validate_phone_valid(self):
        """Test validate_phone with valid phone numbers"""
        valid_phones = [
            "+48123456789",
            "+1-555-123-4567",
            "+33 1 23 45 67 89",
            "123456789",
            "555-123-4567"
        ]
        
        for phone in valid_phones:
            # Should not raise exception
            validate_phone(phone)

    def test_validate_phone_invalid(self):
        """Test validate_phone with invalid phone numbers"""
        invalid_phones = [
            "abc123",
            "",
            None,
            "123",  # Too short
            "12345678901234567890"  # Too long
        ]
        
        for phone in invalid_phones:
            with pytest.raises(ValueError, match="Invalid phone format"):
                validate_phone(phone)

    def test_validate_required_fields_valid(self):
        """Test validate_required_fields with valid data"""
        data = {"name": "Test", "email": "test@example.com", "age": 25}
        required_fields = ["name", "email"]
        
        # Should not raise exception
        validate_required_fields(data, required_fields)

    def test_validate_required_fields_missing(self):
        """Test validate_required_fields with missing fields"""
        data = {"name": "Test", "age": 25}
        required_fields = ["name", "email", "phone"]
        
        with pytest.raises(ValueError, match="Missing required fields: email, phone"):
            validate_required_fields(data, required_fields)

    def test_validate_required_fields_empty_data(self):
        """Test validate_required_fields with empty data"""
        data = {}
        required_fields = ["name", "email"]
        
        with pytest.raises(ValueError, match="Missing required fields: name, email"):
            validate_required_fields(data, required_fields)

    def test_validate_required_fields_no_requirements(self):
        """Test validate_required_fields with no required fields"""
        data = {"name": "Test"}
        required_fields = []
        
        # Should not raise exception
        validate_required_fields(data, required_fields)

    def test_complex_validation_scenario(self):
        """Test complex validation scenario with multiple validators"""
        # Test data that should pass all validations
        params = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+48123456789",
            "age": 30,
            "active": True
        }
        
        required = ["name", "email", "phone"]
        optional = {"age": int, "active": bool, "notes": str}
        
        # Should not raise any exceptions
        validate_parameters(params, required, optional)
        validate_email(params["email"])
        validate_phone(params["phone"])
        validate_required_fields(params, required)

    def test_edge_case_whitespace_values(self):
        """Test validation with whitespace-only values"""
        params = {"field1": "   ", "field2": "\t\n", "field3": "value"}
        required = ["field1", "field2", "field3"]
        
        with pytest.raises(ValueError, match="Missing required parameters: field1, field2"):
            validate_parameters(params, required)

    def test_edge_case_zero_values(self):
        """Test validation with zero values"""
        params = {"field1": 0, "field2": 0.0, "field3": False}
        required = ["field1", "field2", "field3"]
        
        # Should not raise exception (0 and False are valid values)
        validate_parameters(params, required)

    def test_type_validation_edge_cases(self):
        """Test type validation edge cases"""
        params = {"field1": "123", "field2": 123.0, "field3": 1}
        optional = {"field1": str, "field2": float, "field3": bool}
        
        # Should not raise exception for field1 and field2
        # field3 should fail (int is not bool)
        with pytest.raises(ValueError, match="Invalid type for parameter field3"):
            validate_parameters(params, [], optional)