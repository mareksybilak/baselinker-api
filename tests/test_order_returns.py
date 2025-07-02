import pytest
import json
from unittest.mock import Mock, patch
from baselinker import BaseLinkerClient


class TestOrderReturns:
    
    @patch('requests.Session.post')
    def test_add_order_return(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "SUCCESS",
            "return_id": 12345
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        return_data = {
            "order_id": 123,
            "return_reason": "Damaged item",
            "return_status": 1,
            "admin_comments": "Customer reported damage on arrival",
            "products": [
                {
                    "order_product_id": 456,
                    "quantity": 1,
                    "reason": "Item arrived damaged"
                }
            ]
        }
        result = client.returns.add_order_return(**return_data)
        
        assert result["status"] == "SUCCESS"
        assert result["return_id"] == 12345
        
        expected_data = {
            'method': 'addOrderReturn',
            'parameters': json.dumps(return_data)
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_get_order_returns(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "returns": [
                {
                    "return_id": 12345,
                    "order_id": 123,
                    "return_status": 1,
                    "return_reason": "Damaged item",
                    "date_add": 1640995200,
                    "admin_comments": "Customer reported damage",
                    "products": [
                        {
                            "order_product_id": 456,
                            "quantity": 1,
                            "reason": "Item arrived damaged"
                        }
                    ]
                },
                {
                    "return_id": 12346,
                    "order_id": 124,
                    "return_status": 2,
                    "return_reason": "Wrong size",
                    "date_add": 1641081600,
                    "products": [
                        {
                            "order_product_id": 789,
                            "quantity": 1,
                            "reason": "Size too small"
                        }
                    ]
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.returns.get_order_returns(date_from=1640995200)
        
        assert "returns" in result
        assert len(result["returns"]) == 2
        assert result["returns"][0]["return_id"] == 12345
        assert result["returns"][1]["return_reason"] == "Wrong size"
        
        expected_data = {
            'method': 'getOrderReturns',
            'parameters': json.dumps({"date_from": 1640995200})
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_set_order_return_fields(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        update_data = {
            "return_id": 12345,
            "admin_comments": "Return approved - refund processed",
            "return_reason": "Quality issue - approved for refund"
        }
        result = client.returns.set_order_return_fields(**update_data)
        
        assert result["status"] == "SUCCESS"
        
        expected_data = {
            'method': 'setOrderReturnFields',
            'parameters': json.dumps(update_data)
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_set_order_return_status(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"status": "SUCCESS"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.returns.set_order_return_status(
            return_id=12345,
            return_status=3  # Assuming 3 = Completed
        )
        
        assert result["status"] == "SUCCESS"
        
        expected_data = {
            'method': 'setOrderReturnStatus',
            'parameters': json.dumps({
                "return_id": 12345,
                "return_status": 3
            })
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )
    
    @patch('requests.Session.post')
    def test_comprehensive_return_workflow(self, mock_post):
        # Test complete return workflow from creation to completion
        mock_response = Mock()
        mock_post.return_value = mock_response
        mock_response.raise_for_status.return_value = None
        
        client = BaseLinkerClient("test-token")
        
        # Step 1: Create return
        mock_response.json.return_value = {"status": "SUCCESS", "return_id": 99999}
        complex_return = {
            "order_id": 9999,
            "return_reason": "Multiple issues",
            "return_status": 1,
            "admin_comments": "Customer reported multiple problems",
            "products": [
                {
                    "order_product_id": 1001,
                    "quantity": 2,
                    "reason": "Defective units"
                },
                {
                    "order_product_id": 1002,
                    "quantity": 1,
                    "reason": "Wrong color sent"
                }
            ],
            "return_address": {
                "name": "Returns Department",
                "company": "Test Company",
                "street": "Return Street 123",
                "city": "Warsaw",
                "postcode": "00-123",
                "country": "PL"
            }
        }
        result = client.returns.add_order_return(**complex_return)
        assert result["status"] == "SUCCESS"
        assert result["return_id"] == 99999
        
        # Step 2: Update return fields
        mock_response.json.return_value = {"status": "SUCCESS"}
        update_fields = {
            "return_id": 99999,
            "admin_comments": "Return received and inspected - approved",
            "return_reason": "Quality control issues confirmed"
        }
        result = client.returns.set_order_return_fields(**update_fields)
        assert result["status"] == "SUCCESS"
        
        # Step 3: Change status to completed
        result = client.returns.set_order_return_status(return_id=99999, return_status=3)
        assert result["status"] == "SUCCESS"
    
    @patch('requests.Session.post')
    def test_get_returns_with_filters(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {
            "returns": [
                {
                    "return_id": 555,
                    "order_id": 777,
                    "return_status": 2,
                    "return_reason": "Size issue",
                    "date_add": 1641168000
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        client = BaseLinkerClient("test-token")
        result = client.returns.get_order_returns(
            date_from=1641081600,
            date_to=1641254400,
            return_status=2,
            order_id=777
        )
        
        assert "returns" in result
        assert len(result["returns"]) == 1
        assert result["returns"][0]["return_status"] == 2
        assert result["returns"][0]["order_id"] == 777
        
        expected_data = {
            'method': 'getOrderReturns',
            'parameters': json.dumps({
                "date_from": 1641081600,
                "date_to": 1641254400,
                "return_status": 2,
                "order_id": 777
            })
        }
        mock_post.assert_called_with(
            "https://api.baselinker.com/connector.php",
            data=expected_data,
            timeout=30
        )