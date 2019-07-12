import json


def lambda_handler(event, context):
    telegram_message_raw = event['body']
    telegram_message = json.loads(telegram_message_raw)
    print(telegram_message['message'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def get_chat(body):
    return {
        'chat_id': chat_id,
        'text': 'Okay'
    }
