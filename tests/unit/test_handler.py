import json
import pytest
from app import lambda_handler

@pytest.fixture()
def apigw_event():
    return {
        "body": '{ "test": "body"}',
        "httpMethod": "GET",
        "path": "/hello"
    }

def test_lambda_handler(apigw_event):
    response = lambda_handler(apigw_event, "")
    data = json.loads(response["body"])
    assert response["statusCode"] == 200
    assert "views" in data
    assert isinstance(data["views"], int)