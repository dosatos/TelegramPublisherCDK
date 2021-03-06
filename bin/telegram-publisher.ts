#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { TelegramPublisherStack } from '../lib/telegram-publisher-stack';

const app = new cdk.App();
new TelegramPublisherStack(app, 'TelegramPublisherStack');
