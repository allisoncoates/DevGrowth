# created by Allison with help from Gemini

import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DevGrowth')

def lambda_handler(event, context):
    try:
        # We will look for parameters in the Query String (e.g. ?userId=X&date=Y)
        params = event.get('queryStringParameters', {})
        
        user_id = params.get('userId')
        date = params.get('date')

        if not user_id or not date:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
                },
                'body': json.dumps({'message': 'Missing userId or date'})
            }

        # Perform the delete
        table.delete_item(
            Key={
                'User ID': user_id,
                'Date': date
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
            },
            'body': json.dumps({'message': 'Deleted successfully'})
        }

    except ClientError as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
            },
            'body': json.dumps({'error': str(e)})
        }