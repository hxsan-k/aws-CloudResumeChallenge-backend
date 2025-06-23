import json
import boto3
import os
from botocore.exceptions import ClientError
from decimal import Decimal

def lambda_handler(event, context):
    table_name = os.environ.get("TABLE_NAME", "ViewCounterTable")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(Key={'id': 'counter'})
        count = response.get('Item', {}).get('views', 0)

        if isinstance(count, Decimal):
            count = int(count)

        count += 1
        table.put_item(Item={'id': 'counter', 'views': count})

        return {
            'statusCode': 200,
            'body': json.dumps({'views': count})
        }

    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Something went wrong'})
        }
