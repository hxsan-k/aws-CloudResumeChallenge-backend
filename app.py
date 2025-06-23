import json
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ViewCounterTable')

def lambda_handler(event, context):
    try:
        response = table.get_item(Key={'id': 'counter'})
        count = response.get('Item', {}).get('views', 0)

        # DynamoDB returns Decimal, convert it to int
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
# xyz
# Trigger workflow
