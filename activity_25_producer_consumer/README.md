# Activity 25

## The Producer and Consumer Problem

## Instructions

The producer/consumer is a classical problem in distributed computing and used in typical serverless scenarios where parts of the program generate tasks (the producers) and other parts run the tasks (the consumers). This scenario requires a message queue so the producers can interact with the consumers asynchronoulsy. 
 
## Steps

### Step 1 - Package the Producer Application

Use virtualenv to properly package the producer application. The only external library that is needed is boto3. Use the following to zip the application. 

```
zip -r producer.zip \
    producer.py \
    boto3 \
    botocore \
    dateutil \
    jmespath \
    s3transfer \
    urllib3
```

### Step 2 - Create a Message Queuing Service 

Name it activity25. Copy its arn to use on the next step. 

### Step 3 - Create a Policy 

Name it Activity25QueueFullAccess and use the arn that you copied in the previous step. The policy should look like the following: 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "sqs:*",
            "Resource": "arn:aws:sqs:us-west-1:939096940193:activity25"
        }
    ]
}
```

### Step 4 - Create a Role

Name it Activity25Role and attach to the role the folowing policies: 

* Activity25QueueFullAccess (the one you created in previous step) and 
* AWS-managed policy AWSLambdaBasicExecutionRole. 

### Step 5 - Create the Producer Lambda Function

Use what you've learned previously to create a lambda function named producer. Under permissions, select "Use an existing role" as its execution role for the lambda function. Select Activity25Role. Then upload producer.zip.  Don't forget to edit the "Runtime settings" and change the handler of your lambda function to: "producer.lambda_handler. Also, configure environment variables accordingly (QUEUE_URL with the correct queue's URL).

### Step 6 - Test the Producer Lambda Function 

Invoke the lambda function as many times as you want using: 

```
aws lambda invoke --function-name producer /dev/stdout
```

Go to SQS and check that messages were enqueued. 

### Step 7 - Create the Consumer Lambda Function

Name your function consumer this time. Under permissions, select "Use an existing role" as its execution role for the lambda function. Select Activity25Role. Because this lambda function is so simple, there is no need to packaging. Just use the following code: 

```
def lambda_handler(event, context):

    # get message packaged in event
    for record in event['Records']:
        payload = record["body"]
        return { 
            'message' : str(payload)
        }
```

### Step 8 - Add an SQS Trigger 

The SQS trigger will be used to invoke function consumer automatically whenever a new message arrives in activity25 queue. Select the queue when you create the trigger. Notice that right after you create the trigger, all messages get consumed from the queue. Now got to the consumer's function logs. There you should be able to see all invocations of the consumer function.  