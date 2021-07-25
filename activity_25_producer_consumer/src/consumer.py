# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 25 - Write a message to a queue

def lambda_handler(event, context):

    # get message packaged in event
    for record in event['Records']:
        payload = record["body"]
        return { 
            'message' : str(payload)
        }

