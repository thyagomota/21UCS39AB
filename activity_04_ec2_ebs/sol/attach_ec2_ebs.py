# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 04 - Create an EBS Volume and Attach it to an EC2 Instance

import boto3
import time

if __name__ == "__main__":

    # preconditions: 
    INSTANCE_ID = 'i-033aeaf417c8d7918'
    AZ          = 'us-west-1c'
    
    client = boto3.client('ec2')
    
    # TODO: Create an EBS Volume
    volume_id = client.create_volume(
        AvailabilityZone = AZ, 
        VolumeType = 'gp2', 
        Size = 1)['VolumeId']
    print(volume_id)

    # wait for 1 minute for volume to become available
    print('Waiting for volume to become available...')
    time.sleep(60)

    # TODO: Attach the EBS Volume to the EC2 Instance
    client.attach_volume(
        Device = '/dev/sdb',
        InstanceId = INSTANCE_ID, 
        VolumeId = volume_id
    )
 
    # terminate ec2 instance
    # client.terminate_instances( 
    #     InstanceIds = [ instance_id ]
    # )