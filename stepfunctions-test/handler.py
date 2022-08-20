from __future__ import annotations

from logging import getLogger, INFO
from typing import Any

from aws_lambda_powertools.utilities.typing import LambdaContext


logger = getLogger()
logger.setLevel(INFO)

def first_lambda(event: dict[str, Any], context: LambdaContext):
    logger.info(event)

    response = {
        "statusCode": 200,
        "body": "whatever you want."
    }

    return response
