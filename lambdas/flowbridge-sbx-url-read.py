import json
import os
test_eugin="Eugin-PC";

eugin=os.getenv('TEST_EUGIN')
rds_host = os.getenv('RDS_HOST')
rds_port = os.getenv('RDS_PORT')
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS"
            },
            "message": "flowbridge-sbx-url-read deployed from  Actions"
        })
    }