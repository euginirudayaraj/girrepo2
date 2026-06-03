import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "flowbridge-sbx-grafana-write deployed from GitHub Actions"
        })
    }