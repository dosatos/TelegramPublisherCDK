import { expect as expectCDK, matchTemplate, MatchStyle } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import * as TelegramPublisher from '../lib/telegram-publisher-stack';

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new TelegramPublisher.TelegramPublisherStack(app, 'MyTestStack');
    // THEN
    expectCDK(stack).to(matchTemplate({
      "Resources": {}
    }, MatchStyle.EXACT))
});
