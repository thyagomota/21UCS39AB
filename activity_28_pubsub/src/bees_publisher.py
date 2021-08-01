# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 27 - The Bees Publisher

from datetime import datetime
import boto3
import os
import random

# parameters
TOPIC_ARN = os.getenv("TOPIC_ARN")
MESSAGES = [
    "bees are pollinators",  
    "bees produce honey",  
    "all worker bees are female",  
    "bees have 5 eyes",  
    "bees fly about 20mph" ] 

def lambda_handler(event, context):

    # get today's date and time
    today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    
    # attempt to publish message
    sns = boto3.client("sns")
    msg = "\"" + MESSAGES[random.randrange(len(MESSAGES))] + "\" sent on " + today
    sns.publish(
        TopicArn = TOPIC_ARN, 
        Message=msg)

    # return success
    return {
        'statusCode': 200,
        'body': msg
    }

