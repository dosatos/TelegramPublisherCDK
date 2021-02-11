#!/usr/bin/env bash
source telegram_lambda/.env
#echo $test_telegram_token
# shellcheck disable=SC2154
echo $value

aws lambda update-function-configuration --function-name TelegramPublisherStack-TelegramPublisherLambdaEF37-1CBTE2Y6DLQJ4 \
 --environment '{"Variables": {"test_telegram_token":"'$test_telegram_token'", "test_chat":"'$test_chat'"}}'