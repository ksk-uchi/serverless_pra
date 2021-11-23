import boto3
import fire
import json


def hello(event, context):
    body = {
        "message": "This is hello lambda",
    }
    print(json.dumps(event))

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


def my_queue(event, context):
    for record in event["Records"]:
        print(record["body"])
    # raise Exception("to fail")


def sqs_send(message):

    # Get the service resource
    sqs = boto3.resource('sqs', region_name="us-east-1")

    # Get the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName='KSKQueue')

    response = queue.send_message(MessageBody=message)
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))

    response2 = queue.send_message(MessageBody='boto3', MessageAttributes={
        'Author': {
            'StringValue': 'Daniel',
            'DataType': 'String'
        }
    })
    print(response2.get('MessageId'))
    print(response2.get('MD5OfMessageBody'))


def sqs_send(message):

    # Get the service resource
    sqs = boto3.resource('sqs', region_name="us-east-1")

    # Get the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName='KSKQueue')

    response = queue.send_message(MessageBody=message)
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))

    response2 = queue.send_message(MessageBody='boto3', MessageAttributes={
        'Author': {
            'StringValue': 'Daniel',
            'DataType': 'String'
        }
    })
    print(response2.get('MessageId'))
    print(response2.get('MD5OfMessageBody'))


def sqs_receive():

    # Get the service resource
    sqs = boto3.client('sqs', region_name="us-east-1")

    # Get the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName='KSKQueue')

    # import pdb;pdb.set_trace()
    # ...


if __name__ == "__main__":
    fire.Fire()
