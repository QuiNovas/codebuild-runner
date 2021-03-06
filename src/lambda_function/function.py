import boto3
import logging
import os

from botocore.client import Config


def handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    code_build = boto3.client('codebuild', config=Config(signature_version='s3v4'))

    logger.info('Starting CodeBuild project {}'.format(os.environ['PROJECT_NAME']))
    code_build.start_build(
        projectName=os.environ['PROJECT_NAME']
    )
    logger.info('Started CodeBuild project {}'.format(os.environ['PROJECT_NAME']))


    return event
