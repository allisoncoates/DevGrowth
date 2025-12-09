# created by Mai
# updated by Allison with help from Gemini

import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DevGrowth')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        
        # We need the Keys to identify WHICH item to update
        user_id = body.get('userId', 'DemoUser') 
        date = body['date']
        
        # The new values
        worked_on = body['workedOn']
        learned = body['learned']
        stuck_on = body['stuckOn']
        
        response = table.update_item(
            Key={
                'User ID': user_id,
                'Date': date
            },
            # We use #w, #l, #s as placeholders because the real names have spaces
            UpdateExpression="SET #w = :w, #l = :l, #s = :s",
            ExpressionAttributeNames={
                '#w': 'Worked On',
                '#l': 'Learned',
                '#s': 'Stuck On'
            },
            ExpressionAttributeValues={
                ':w': worked_on,
                ':l': learned,
                ':s': stuck_on
            },
            ReturnValues="UPDATED_NEW"
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,PUT'
            },
            'body': json.dumps({'message': 'Updated successfully!'})
        }

    except ClientError as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,PUT'
            },
            'body': json.dumps({'error': str(e)})
        }