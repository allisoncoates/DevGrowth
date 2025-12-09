# created by Allison with help from Gemini

import json
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

# Create DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DevGrowth') 

def lambda_handler(event, context):
    # Default user if none is provided
    user_id = "DemoUser" 
    
    # Check if the frontend sent a userId in the URL parameters
    if event.get('queryStringParameters') and event['queryStringParameters'].get('userId'):
        user_id = event['queryStringParameters']['userId']

    try:
        # Query the table for all items with this User ID
        response = table.query(
            KeyConditionExpression=Key('User ID').eq(user_id)
        )
        
        items = response.get('Items', [])

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps(items)
        }

    except ClientError as e:
        print(f"Error fetching items: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'error': str(e)})
        }