import * as cdk from '@aws-cdk/core';

import * as path from 'path';
import * as Lambda from "@aws-cdk/aws-lambda";


export class TelegramPublisherStack extends cdk.Stack {
    constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        // Configure path to Dockerfile
        const dockerfile = path.join(__dirname, "../telegram_lambda");

        // Create AWS Lambda function and push image to ECR
        const telegramPublisherLambda = new Lambda.DockerImageFunction(this, "TelegramPublisherLambda", {
            code: Lambda.DockerImageCode.fromImageAsset(dockerfile),
        });
    }
}
