# created by Mai with help from ChatGPT
# updated by Allison with help from Gemini

import json
import boto3
from botocore.exceptions import ClientError

# Create a DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DevGrowth')

def lambda_handler(event, context):
    try:
        # Parse the incoming JSON body
        body = json.loads(event['body'])
        
        user_id = body['userId']
        worked_on = body['workedOn']
        date = body['date']
        learned = body['learned']
        stuck_on = body['stuckOn']
        
        # Insert data into DynamoDB
        response = table.put_item(
            Item={
                'User ID': user_id,
                'Date': date,  # date is the sort key
                'Worked On': worked_on,
                'Learned': learned,
                'Stuck On': stuck_on
            }
        )

        # Return success response with CORS headers
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({
                'message': 'Progress added successfully!',
                'item': response.get('Attributes', {})
            })
        }

    except ClientError as e:
        # Handle errors from DynamoDB
        print(f"Error adding item: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({
                'message': 'Failed to add progress',
                'error': e.response['Error']['Message']
            })
        }

    except Exception as e:
        # Handle other unexpected exceptions
        print(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({
                'message': 'Internal Server Error',
                'error': str(e)
            })
        }