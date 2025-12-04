import json
import boto3
from botocore.exceptions import ClientError

# Create a DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DevGrowth') 

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        user_id = body['userId']
        worked_on = body['workedOn']
        date = body['date']
        learned = body['learned']
        stuck_on = body['stuckOn']
        
        # 
        response = table.update_item(
            Key={
                'User ID': user_id,
                'Date': date  # date is sort key
            },
            UpdateExpression="SET Worked On = :worked_on, Learned = :learned, Stuck On = :stuck_on",
            ExpressionAttributeValues={
                ':worked_on': worked_on,
                ':learned': learned,
                ':stuck_on': stuck_on
            },
            ReturnValues="UPDATED_NEW"  # Returns the new values of the updated attributes
        )

        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Progress updated successfully!',
                'updatedAttributes': response['Attributes']
            })
        }

    except ClientError as e:
        # Handle errors from DynamoDB
        print(f"Error updating item: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Failed to update progress',
                'error': e.response['Error']['Message']
            })
        }

    except Exception as e:
        # Handle other exceptions
        print(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Internal Server Error',
                'error': str(e)
            })
        }
