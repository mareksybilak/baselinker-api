# Contributing to BaseLinker API Python Client

Thank you for your interest in contributing to the BaseLinker API Python client! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Code Style](#code-style)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)
- [Release Process](#release-process)

## Code of Conduct

This project follows a simple code of conduct:

- Be respectful and inclusive
- Focus on constructive feedback
- Help maintain a welcoming environment
- Report any concerning behavior to the maintainers

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- Basic knowledge of BaseLinker API
- Familiarity with Python packaging and testing

### Types of Contributions

We welcome several types of contributions:

- **Bug reports**: Help us identify and fix issues
- **Feature requests**: Suggest new functionality
- **Code contributions**: Implement fixes or new features
- **Documentation**: Improve or expand documentation
- **Tests**: Add or improve test coverage
- **Examples**: Provide real-world usage examples

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/your-username/baselinker-api.git
cd baselinker-api

# Add upstream remote
git remote add upstream https://github.com/original-username/baselinker-api.git
```

### 2. Create Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install package in editable mode
pip install -e .
```

### 3. Verify Setup

```bash
# Run tests to ensure everything works
pytest

# Check code style
black --check baselinker/
flake8 baselinker/

# Run type checking
mypy baselinker/
```

## Making Changes

### Branch Strategy

1. Create a feature branch from `main`:

```bash
git checkout main
git pull upstream main
git checkout -b feature/your-feature-name
```

2. Use descriptive branch names:
   - `feature/add-webhook-support`
   - `bugfix/fix-rate-limit-handling`
   - `docs/improve-api-examples`
   - `test/add-integration-tests`

### Commit Guidelines

1. Write clear, descriptive commit messages:

```bash
# Good commit messages
git commit -m "Add support for webhook endpoints"
git commit -m "Fix rate limit error handling in client"
git commit -m "Update README with new authentication examples"

# Poor commit messages
git commit -m "Fix bug"
git commit -m "Update code"
git commit -m "Changes"
```

2. Make atomic commits (one logical change per commit)
3. Use present tense ("Add feature" not "Added feature")
4. Reference issues when applicable: "Fix order status update (#42)"

### Code Organization

- **New API methods**: Add to `baselinker/client.py`
- **New exceptions**: Add to `baselinker/exceptions.py`
- **Tests**: Add to appropriate test file in `tests/`
- **Examples**: Add to `examples/` directory
- **Documentation**: Add to `docs/` directory

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=baselinker --cov-report=term-missing

# Run specific test file
pytest tests/test_client.py -v

# Run specific test
pytest tests/test_client.py::TestBaseLinkerClient::test_successful_request -v
```

### Writing Tests

1. **Test file naming**: `test_*.py`
2. **Test class naming**: `TestClassName`
3. **Test method naming**: `test_method_description`

Example test structure:

```python
import pytest
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient
from baselinker.exceptions import APIError

class TestNewFeature:
    
    @patch('requests.Session.post')
    def test_new_method_success(self, mock_post):
        # Setup
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        
        # Execute
        result = client.new_method(param1="value1")
        
        # Assert
        assert result["status"] == "SUCCESS"
        mock_post.assert_called_once()
    
    @patch('requests.Session.post')
    def test_new_method_error(self, mock_post):
        # Test error conditions
        mock_response = Mock()
        mock_response.json.return_value = {
            "error_code": "ERROR_INVALID_PARAM",
            "error_message": "Invalid parameter"
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        
        with pytest.raises(APIError) as exc_info:
            client.new_method(param1="invalid")
        
        assert exc_info.value.error_code == "ERROR_INVALID_PARAM"
```

### Test Requirements

- **Unit tests**: Test individual methods and functions
- **Integration tests**: Test complete workflows
- **Error handling**: Test all error conditions
- **Edge cases**: Test boundary conditions and unusual inputs
- **Coverage**: Maintain 90%+ test coverage

## Code Style

### Python Style Guide

We follow PEP 8 with some specific conventions:

```python
# Import order
import json
import os
from typing import Dict, Any, Optional

import requests

from .exceptions import BaseLinkerError

# Function definitions
def method_name(self, required_param: str, optional_param: int = None) -> Dict[str, Any]:
    """
    Brief description of the method.
    
    Args:
        required_param: Description of required parameter
        optional_param: Description of optional parameter
        
    Returns:
        Dictionary with API response data
        
    Raises:
        AuthenticationError: When token is invalid
        APIError: When API returns error
    """
    pass

# Constants
API_BASE_URL = "https://api.baselinker.com"
DEFAULT_TIMEOUT = 30

# Class definitions
class ExampleClass:
    """Example class with proper docstring."""
    
    def __init__(self, param: str):
        self.param = param
```

### Code Formatting

Use the provided development tools:

```bash
# Format code with black
black baselinker/ tests/ examples/

# Sort imports
isort baselinker/ tests/ examples/

# Check style with flake8
flake8 baselinker/ tests/

# Type checking with mypy
mypy baselinker/
```

### Configuration Files

The project includes configuration for development tools:

- `.flake8`: Flake8 configuration
- `pyproject.toml`: Black and isort configuration
- `mypy.ini`: MyPy configuration

## Documentation

### Docstring Format

Use Google-style docstrings:

```python
def example_method(self, param1: str, param2: int = None) -> Dict[str, Any]:
    """
    Brief description of what the method does.
    
    Longer description with more details about the method's purpose,
    behavior, and any important notes.
    
    Args:
        param1: Description of the first parameter
        param2: Optional parameter with default value
        
    Returns:
        Dictionary containing:
            - key1: Description of key1
            - key2: Description of key2
            
    Raises:
        AuthenticationError: When authentication fails
        RateLimitError: When rate limit is exceeded
        APIError: For other API-related errors
        
    Example:
        >>> client = BaseLinkerClient("token")
        >>> result = client.example_method("value", 42)
        >>> print(result["key1"])
    """
```

### Documentation Updates

When adding new features, update:

1. **README.md**: Add to appropriate section
2. **docs/api_methods.md**: Document new API methods
3. **docs/examples.md**: Add usage examples
4. **Docstrings**: Add comprehensive docstrings

## Submitting Changes

### Before Submitting

1. **Test your changes**:
   ```bash
   pytest
   pytest --cov=baselinker
   ```

2. **Check code style**:
   ```bash
   black --check baselinker/ tests/
   flake8 baselinker/ tests/
   mypy baselinker/
   ```

3. **Update documentation** if needed

4. **Update changelog** for significant changes

### Pull Request Process

1. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request** on GitHub with:
   - Clear title describing the change
   - Detailed description of what was changed and why
   - Reference to any related issues
   - Screenshots/examples if applicable

3. **Pull Request Template**:
   ```markdown
   ## Description
   Brief description of changes made.
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Performance improvement
   - [ ] Code refactoring
   
   ## Testing
   - [ ] Tests pass locally
   - [ ] Added tests for new functionality
   - [ ] Updated documentation
   
   ## Related Issues
   Fixes #123
   
   ## Checklist
   - [ ] Code follows project style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   - [ ] Tests added/updated
   ```

4. **Respond to feedback** and make requested changes

5. **Squash commits** if requested before merge

### Review Process

- Maintainers will review your pull request
- Automated tests must pass
- At least one maintainer approval required
- All feedback must be addressed
- Documentation and tests required for new features

## Release Process

### Version Numbering

We use Semantic Versioning (SemVer):
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

For maintainers preparing releases:

1. **Update version** in `setup.py` and `__init__.py`
2. **Update CHANGELOG.md** with release notes
3. **Run full test suite**:
   ```bash
   pytest --cov=baselinker
   ```
4. **Build and test package**:
   ```bash
   python -m build
   pip install dist/baselinker-api-*.whl
   ```
5. **Create release tag**:
   ```bash
   git tag v1.2.3
   git push origin v1.2.3
   ```
6. **Create GitHub release** with release notes
7. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

## Getting Help

### Communication Channels

- **GitHub Issues**: For bugs, feature requests, and questions
- **GitHub Discussions**: For general questions and discussions
- **Pull Request Comments**: For code-specific discussions

### Resources

- [BaseLinker API Documentation](https://api.baselinker.com)
- [Python Packaging Guide](https://packaging.python.org/)
- [Pytest Documentation](https://docs.pytest.org/)
- [PEP 8 Style Guide](https://pep8.org/)

### Common Issues

**Q: Tests fail with "No module named 'baselinker'"**
A: Install package in editable mode: `pip install -e .`

**Q: Import errors when running examples**
A: Make sure you've activated your virtual environment and installed dependencies

**Q: How do I test against real API?**
A: Use a test BaseLinker account and set environment variables. Never test against production data.

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes for significant contributions
- GitHub contributors graph

Thank you for contributing to the BaseLinker API Python client!