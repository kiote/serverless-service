import json

def lambda_handler(event, context):
    telegram_message_raw = event['body']
    telegram_message = json.loads(telegram_message_raw)
    print(telegram_message['message'])
    print(telegram_message['message']['chat']['id'])
    return {
        'statusCode': 200,
        'body': json.dumps(get_chat(telegram_message))
    }

def get_chat(body):
    message = body['message']
    chat_id = message['chat']['id']
    return {
        'chat_id': chat_id,
        'text': 'you said: ' + message['text']
    }
