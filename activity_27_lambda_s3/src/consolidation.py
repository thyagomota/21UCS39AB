# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 26 - Consolidates in/out inventory data

import os
import boto3

# parameters
BUCKET_DESTINATION = os.getenv("BUCKET_DESTINATION")

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    for record in event['Records']:
        if record['eventSource'] == 'aws:s3':
            s3_info = record['s3']
            bucket = s3_info['bucket']['name']
            object_key = s3_info['object']['key']
            try:
                os.chdir('/tmp')
                print('trying to download file...')
                print(bucket)
                print(object_key)
                s3.download_file(bucket, object_key, object_key)
                print('trying to delete file...')
                s3.delete_object(
                    Bucket = bucket,
                    Key = object_key)
                with open(object_key, 'rt') as csv:
                    items = {}
                    for line in csv:
                        line = line.strip()
                        item, in_out = line.split(',')
                        if item not in items:
                            items[item] = 0
                        items[item] += int(in_out)
                with open(object_key, 'wt') as csv:
                    for item in items:
                        csv.write(item + ',' + str(items[item]) + '\n')
                print('trying to upload file...')
                s3.upload_file(object_key, BUCKET_DESTINATION, object_key)
            except Exception as ex: 
                print(ex)
                return {
                    'statusCode': 200,
                    'body': 'unexpected errors happened!'
                }
        else:
            return {
                        'statusCode': 200,
                        'body': 'Not an s3 event!'
                    }
    return {
        'statusCode': 200,
        'body': 'success!'
    }

