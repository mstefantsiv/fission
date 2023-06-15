import boto3 as boto
import logging


def process_sqs_message(message):
    # Process the message
    message_body = message['Body']
    logging.info(f"Received message: {message_body}")

    # Add your processing logic here

    # Return True if processing is successful, False otherwise
    return True


def lock_sqs_message(sqs_client, receipt_handle, visibility_timeout):
    # Change the visibility timeout of the message to lock it
    response = sqs_client.change_message_visibility(
        QueueUrl='https://sqs.us-east-2.amazonaws.com/825155998022/q_trigger',
        ReceiptHandle=receipt_handle,
        VisibilityTimeout=visibility_timeout
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        logging.info("Message locked successfully")
    else:
        logging.error("Failed to lock message")


def delete_sqs_message(sqs_client, receipt_handle):
    # Delete the message
    response = sqs_client.delete_message(
        QueueUrl='https://sqs.us-east-2.amazonaws.com/825155998022/q_trigger',
        ReceiptHandle=receipt_handle
    )

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        logging.info("Message deleted successfully")
    else:
        logging.error("Failed to delete message")


def wait_and_process_sqs_message(sqs_client):
    # Receive a message from the SQS queue
    response = sqs_client.receive_message(
        QueueUrl='https://sqs.us-east-2.amazonaws.com/825155998022/q_trigger',
        AttributeNames=['All'],
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20
    )

    # Check if a message was received
    if 'Messages' in response:
        message = response['Records'][0]
        receipt_handle = message['receiptHandle']

        # Process the message
        if process_sqs_message(message):
            # Delete the message if processing is successful
            lock_sqs_message(sqs_client, receipt_handle, 5)
        else:
            logging.error("Failed to process message")

    else:
        logging.info("No messages in the queue")


def main():
    sqs_client = boto.client(
        'sqs',
        region_name='us-east-2',
        aws_access_key_id='AKIA4AHZBKFDNIFTTL5P',
        aws_secret_access_key='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'
    )
    wait_and_process_sqs_message(sqs_client)
    return "HI!"
