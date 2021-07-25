# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 25 - Write a message to a queue

from datetime import datetime
import boto3
import os

# parameters
QUEUE_URL = os.getenv("QUEUE_URL")

def lambda_handler(event, context):

    # get today's date and time
    today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    
    # attempt to write to message queue 
    sqs = boto3.client("sqs")
    sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=today)

