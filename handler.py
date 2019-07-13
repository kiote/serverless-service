import json
import os
from botocore.vendored import requests
import boto3

def lambda_handler(event, context):
    telegram_message_raw = event['body']
    telegram_message = json.loads(telegram_message_raw)
    send_reponse(telegram_message)
    client = boto3.client('dynamodb')
    chat_id = "12"
    ttl = "1563580800"
    message = 'Call Me Today'
    response = client.put_item(
        TableName='realestate_messages',
        Item={
            'chat_id': {
                'S': chat_id,
            },
            'ttl': {
                'N': ttl,
            },
            'message': {
                'S': message,
            },
        },
    )
    return {
        'statusCode': 200,
        'body': json.dumps("all good")
    }


def send_reponse(body):
    message = body['message']
    chat_id = message['chat']['id']
    url = "https://api.telegram.org/" + \
        os.environ['BOT_AUTH'] + "/sendMessage?"
    params = {
        'chat_id': chat_id,
        'text': 'you said: ' + message['text']
    }
    url += "chat_id=" + str(params['chat_id'])
    url += "&text=" + params['text']
    requests.get(url)
