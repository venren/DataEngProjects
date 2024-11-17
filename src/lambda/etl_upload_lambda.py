import json
import boto3

def helloLambda(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Extract bucket name and file key from the event
    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        print(f"File '{file_key}' was uploaded to bucket '{bucket_name}'.")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Processed file '{file_key}' from bucket '{bucket_name}'.",
            })
        }
    
    except KeyError as e:
        print(f"Error extracting bucket or file key: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Invalid S3 event structure."})
        }