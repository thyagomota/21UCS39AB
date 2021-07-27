# Activity 27

## Using S3 as a Trigger for Lambda

## Goal

In this activity we are interested in learning how S3 bucket updates (e.g., a file upload) can trigger a typical data processing lambda function. 
 
## Steps

### Step 1 - Create Buckets

Create 2 buckets, one to be the source of files to be processed (e.g., alpha-vision-1234) and another to be the destination of processed files (e.g., alpha-vision-4321). For the sake of simplicity, enable public access to those buckets and also create bucket policies that would allow full access from everyone. For example: 

```
{
    "Version": "2012-10-17",
    "Id": "Policy1627421329639",
    "Statement": [
        {
            "Sid": "Stmt1627421328681",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::alpha-vision-1234/*"
        }
    ]
}
```

### Step 2 - Create a Lambda Function

Create a lambda function called consolidation using the code in src. Don't forget to configure the BUCKET_DESTINATION environment variable with the names of the destination bucket (e.g., alpha-vision-4321). 

### Step 3 - Create an Event Notification 

On the source bucket, create an event notification (under bucket properties) named consolidation, of type "All object create events", and with the consolidation lambda function as destination. The moment you create this event notification, a new trigger is configured and associated to your lambda function. 

Add an S3 trigger to your lambda function associated with the source bucket. That way, your lambda function will be automatically called whenever a new object is uploaded to the source bucket. 

### Step 4 - Testing 

Upload csv files (like the one in the files folder) to the source bucket. Confirm that the file gets processed and moved to the output bucket. 

### Challenge 

Verify if you can run the same example but using a role attached to the function (instead of a bucket policy). OR, make the bucket policy more restrict (i.e., allowing access to only the lambda function). 
