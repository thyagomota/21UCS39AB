# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 01 - Launch EC2 instance on a public subnet

import boto3
import json
import time

if __name__ == "__main__":

    # TODOd: obtain the id of the default VPC
    client = boto3.client('ec2')
    vpcs = client.describe_vpcs()['Vpcs']
    default_vpc_id = None
    for vpc in vpcs:
        if vpc['IsDefault']:
            default_vpc_id = vpc['VpcId']
            break
    if not default_vpc_id:
        print('There is not default VPC!')
        exit(1)
    print('Default VPC id is ' + default_vpc_id)

    # TODOd: obtain the id of the subnet that has the property MapPublicIpOnLaunch set to true
    filter = {
        'Name': 'vpc-id',
        'Values': [ default_vpc_id ]
    }
    subnets = client.describe_subnets( Filters = [filter])['Subnets']
    public_subnet_id = None
    for subnet in subnets:
        if subnet['MapPublicIpOnLaunch']:
            public_subnet_id = subnet['SubnetId']
            break 
    if not public_subnet_id:
        print('There is no public subnet!')
        exit(1)
    print('Public subnet id is ' + public_subnet_id)

    # TODO: create a security group 
    

    # TODO: add an ingress rule to security group
    

    # TODO: launch ec2 instance 
    

    # wait for 1 minute for instance to be launched
    # print('Waiting for instance to be launched...')
    # time.sleep(60)

    # TODO: get the public IP of your instance
    
 
    # terminate ec2 instance
    # client.terminate_instances( 
    #     InstanceIds = [ instance_id ]
    # )