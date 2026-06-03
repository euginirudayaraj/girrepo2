import json
import os

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "flowbridge-sbx-url-read deployed from GitHub Actions"
        })
    }