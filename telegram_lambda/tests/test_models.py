import pytest

from app import handler
from models import TelegramRequest, TelegramMessageQuery


def test_successful_telegram_request_model():
    message = {
        "token": "TEST_TOKEN",
        "method": "message",
        "query": TelegramMessageQuery(
            chat_name="chat_id",
            text="String"
        ),
    }
    TelegramRequest(**message)


def test_failing_telegram_request_model_whenWrongMethodPassed():
    message = {
        "token": "TEST_TOKEN",
        "method": "nonEnumMessage",
        "query": TelegramMessageQuery(
            chat_name="chat_name",
            text="String"
        ),
    }
    with pytest.raises(ValueError):
        TelegramRequest(**message)


def test_message_not_sent_when_wrong_token_passed():
    events = {
        "token": "WRONG_TOKEN",
        "method": "message",
        "query": {
            "chat_name": "test_chat",
            "text": "String"
        }
    }
    assert handler(events=events, context="context")['status_code'] == 404


def test_message_not_sent_when_wrong_chat_passed():
    events = {
        "token": "test_telegram_token",
        "method": "message",
        "query": {
            "chat_name": "WRONG_CHAT",
            "text": "String"
        }
    }
    assert handler(events=events, context="context")['status_code'] == 400


# def test_sends_message():
#     events = {
#         "token": "test_telegram_token",
#         "method": "message",
#         "query": {
#             "chat_name": "test_chat",
#             "text": "String"
#         }
#     }
#     assert handler(events=events, context="context")['status_code'] == 200
