#!/usr/bin/env bash
source .env
payload='{"token":"test_telegram_token","method":"message","query":{"chat_name":"test_chat","text":"message"}}'
aws lambda invoke \
  --function-name TelegramPublisherStack-TelegramPublisherLambdaEF37-1CBTE2Y6DLQJ4  \
  --payload $payload  \
  --cli-binary-format raw-in-base64-out response.json && cat response.json  && echo ""