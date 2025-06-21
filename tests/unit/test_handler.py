import boto3
import pytest
import json
from moto import mock_dynamodb
from app import lambda_handler

@pytest.fixture()
def apigw_event():
    return {
        "body": '{ "test": "body"}',
        "httpMethod": "GET",
        "path": "/hello"
    }

@mock_dynamodb()
def test_lambda_handler(apigw_event):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
        TableName='ViewCounterTable',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
    )

    table.put_item(Item={'id': 'counter', 'views': 0})

    response = lambda_handler(apigw_event, "")
    body = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert "views" in body
    assert isinstance(body["views"], int)
