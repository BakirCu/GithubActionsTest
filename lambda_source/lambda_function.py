import json

def lambda_handler(event, context):
    print(event)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'data': json.dumps(event)
    }

def capital_case(data):
    return data.capitalize()