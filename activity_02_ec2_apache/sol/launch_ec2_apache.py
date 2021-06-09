# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 02 - Launch EC2 instance w/ Apache Server

import boto3
import time

if __name__ == "__main__":

    # preconditions: 
    DEFAULT_VPC_ID   = 'vpc-924e57f5'
    PUBLIC_SUBNET_ID = 'subnet-b1b256eb'
    
    client = boto3.client('ec2')
    
    # TODOd: create a security group 
    sg_id = client.create_security_group(
        GroupName = 'activity_02',
        Description = 'activity_02',
        VpcId = DEFAULT_VPC_ID)['GroupId']
    print('Security group was created with id ' + sg_id)
   
    # TODO: add ingress rules to security group
    ip_permission_ssh = {
        'FromPort': 22,
        'ToPort':   22,
        'IpProtocol': 'tcp',
        'IpRanges': [ 
            {
                'CidrIp': '0.0.0.0/0',
                'Description': 'ssh access to ec2 instance from anywhere!'
            }
        ]
    }
    ip_permission_http = {
        'FromPort': 80,
        'ToPort':   80,
        'IpProtocol': 'tcp',
        'IpRanges': [ 
            {
                'CidrIp': '0.0.0.0/0',
                'Description': 'http access to ec2 instance from anywhere!'
            }
        ]
    }    
    client.authorize_security_group_ingress(
        GroupId = sg_id, 
        IpPermissions = [ ip_permission_ssh, ip_permission_http ]
    )    

    # TODO: launch ec2 instance 
    user_data = '''#!/bin/bash
yum update -y
yum install httpd -y
systemctl enable httpd
systemctl start httpd
cd /var/www/html
echo "This is INSTANCE ${HOSTNAME}" > index.html'''    
    instance_id = client.run_instances(
        ImageId = 'ami-0b2ca94b5b49e0132',
        MinCount = 1, 
        MaxCount = 1,
        InstanceType = 't2.micro',
        SecurityGroupIds = [ sg_id ],
        SubnetId = PUBLIC_SUBNET_ID, 
        KeyName = 'cs39ab',
        UserData = user_data
    )['Instances'][0]['InstanceId']
    print('Instance id is ' + instance_id)


    # wait for 1 minute for instance to be launched
    print('Waiting for instance to be launched...')
    time.sleep(30)

    # TODO: display the public IP of your instance
    ip_address = client.describe_instances(
        InstanceIds = [ instance_id ]
    )['Reservations'][0]['Instances'][0]['PublicIpAddress']
    print(ip_address)
     
