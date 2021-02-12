import json

from telegram_publisher_lib.models import TelegramRequest
from telegram_publisher_lib.telegram_client import post_message


def handler(events, context):
    request = TelegramRequest(**events)
    response = post_message(request=request)
    return {
        "status_code": response.status_code,
        "message": json.loads(response.content),
    }


# if __name__ == '__main__':
#     events = {
#         "token": "test_telegram_token",
#         "method": "message",
#         "query": {
#             "chat_name": "test_chat",
#             "text": "String"
#         }
#     }
#     print(handler(events, ""))