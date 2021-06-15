# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Homework 01 - Launch EC2 instance w/ Netcat Server

import boto3
import time

if __name__ == "__main__":

    # preconditions: 
    DEFAULT_VPC_ID = 'vpc-924e57f5'
    PUBLIC_SUBNET_ID = 'subnet-b1b256eb'
    
    client = boto3.client('ec2')
    
    # TODO: create a security group 
    

    # TODO: add ingress rules to security group
    

    # TODO: launch ec2 instance 
    

    # wait for 1 minute for instance to be launched
    print('Waiting for instance to be launched...')
    time.sleep(60)

    # TODO: get and display the public IP of your instance
    
