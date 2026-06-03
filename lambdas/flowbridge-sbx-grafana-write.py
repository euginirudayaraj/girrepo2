import json
import os

rds_host = os.getenv('RDS_HOST')
rds_port = os.getenv('RDS_PORT')
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "flowbridge-sbx-grafana-write deployed from GitHub Actions"
        })
    }