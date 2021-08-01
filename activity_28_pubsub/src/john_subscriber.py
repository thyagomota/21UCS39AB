# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 27 - John Subscriber (subscribing to bees topic only)

def lambda_handler(event, context):

    # show any messages that arrived
    messages = []
    for record in event['Records']:
        message = {}
        message['id'] = record['Sns']['MessageId']
        message['TopicArn'] = record['Sns']['TopicArn']
        message['content'] = record['Sns']['Message']
        messages.append(message)
    print(messages)

    # return success
    return {
        'statusCode': 200,
        'body': str(messages)
    }

