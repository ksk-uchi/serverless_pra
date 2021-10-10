import json


def hello(event, context):
    body = {
        "message": "This is hello lambda",
    }

    if event["condition"] == "success":
        return {"statusCode": 200, "body": json.dumps(body)}
    else:
        raise Exception("condition was not success")


def successLambda(event, context):
    body = {
        "message": "successLambda invoked",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}


def failureLambda(event, context):
    body = {
        "message": "failureLambda invoked",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}

aws --region us-east-1 lambda invoke --function-name ksk-test-dev-first --payload '{ "condition": "success" }' out.json