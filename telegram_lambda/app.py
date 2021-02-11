import json

from src.models import TelegramRequest
from src.telegram_client import post_message


def handler(events, context):
    request = TelegramRequest(**events)
    response = post_message(request=request)
    return {
        "status_code": response.status_code,
        "message": json.loads(response.content),
    }
