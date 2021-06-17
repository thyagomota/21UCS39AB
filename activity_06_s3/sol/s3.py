# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 06 - Upload/Download/Delete to/from an S3 Bucket

import boto3
import time

if __name__ == "__main__":
    
    client = boto3.client('s3')
    
    # TODO: Create an S3 Bucket
    # result = client.create_bucket(
    #     Bucket = 'activity-06-ocean-breeze-v11', 
    #     CreateBucketConfiguration = {
    #         'LocationConstraint': 'us-west-1'
    #     }
    # )
    # print(result)

    # TODO: - Upload a File
    # client.upload_file(
    #     Filename = 'files/eagle.jpeg', 
    #     Bucket = 'activity-06-ocean-breeze-v11',
    #     Key = 'eagle.jpeg'
    # )

    # TODO: List Contents of a Bucket
    # contents = client.list_objects(
    #             Bucket = 'activity-06-ocean-breeze-v11',
    # )['Contents']
    # for content in contents:
    #     print(content['Key'])

    # TODO: Download a File
    # with open('files/eagle2.jpeg', 'wb') as f:
    #     client.download_fileobj('activity-06-ocean-breeze-v11', 'eagle.jpeg', f)

    # TODO: Delete a File
    # client.delete_object(
    #     Bucket = 'activity-06-ocean-breeze-v11',
    #     Key = 'eagle.jpeg'        
    # )

    # TODO: Delete bucket
    client.delete_bucket(
        Bucket = 'activity-06-ocean-breeze-v11'
    )

    
