import requests

from src.models import (
    TelegramRequest,
)
from src import query_compiler


def post_message(request: TelegramRequest) -> requests.Response:
    # if request.method == TelegramMethodEnum.message.name:
    return _send_message(request=request)


def _send_message(request: TelegramRequest) -> requests.Response:
    url = f"https://api.telegram.org/bot{query_compiler.get_token(request)}/sendMessage?{query_compiler.compile_query(request.query)}"
    return requests.post(url)
