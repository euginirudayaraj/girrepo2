import json
import os

rds_host = os.getenv('RDS_HOST')
rds_port = os.getenv('RDS_PORT')
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "flowbridge-sbx-url-read deployed from GitHub Actions"
        })
    }