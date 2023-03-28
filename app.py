import json

def start_handler(event, context):
    message = "Hello from Lambda with Python!!!! ver5"

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
