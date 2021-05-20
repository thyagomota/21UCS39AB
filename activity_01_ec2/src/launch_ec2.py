# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 01 - Launch EC2 instance on a public subnet

import boto3
import json
import time

if __name__ == "__main__":

    # TODO: obtain the id of the default VPC
    
    
    # TODO: obtain the id of the subnet that has the property MapPublicIpOnLaunch set to true
    

    # TODO: create a security group 
    

    # TODO: add an ingress rule to security group
    

    # TODO: launch ec2 instance 
    

    # wait for 1 minute for instance to be launched
    print('Waiting for instance to be launched...')
    time.sleep(60)

    # TODO: get the public IP of your instance
    
 
    # terminate ec2 instance
    # client.terminate_instances( 
    #     InstanceIds = [ instance_id ]
    # )