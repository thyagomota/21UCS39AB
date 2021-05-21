# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 04 - Create an EBS Volume and Attach it to an EC2 Instance

import boto3
import time

if __name__ == "__main__":

    # preconditions: 
    INSTANCE_ID = 'i-0c12f821c68a5f301'
    AZ = 'us-west-1c'
    
    client = boto3.client('ec2')
    
    # TODO: Create an EBS Volume
    

    # wait for 1 minute for volume to become available
    print('Waiting for volume to become available...')
    time.sleep(60)

    # TODO: Attach the EBS Volume to the EC2 Instance
    
 
    # terminate ec2 instance
    # client.terminate_instances( 
    #     InstanceIds = [ instance_id ]
    # )