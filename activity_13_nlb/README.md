# Activity 13

## A Network Load Balancer (NLB)

## Goal
The goal of this activity is to illustrate how to create a Network Load Balancer (NLB) in AWS. 

## Steps

### Step 1 - Create an S3 Bucket 

Create an S3 bucket and upload hello.py (from src) and hello.service (from files).  Make sure your bucket allows public access and there is a policy in place to allow access to objects. For example, if you bucket is called scissors-sinners, the policy should be something like: 

```
{
    "Version": "2012-10-17",
    "Id": "Policy1625502319389",
    "Statement": [
        {
            "Sid": "Stmt1625502316441",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::scissors-sinners/*"
        }
    ]
}
```

Don't copy and paste that policy.  Use the policy generator instead. 

### Step 2 - Instantiate EC2 Instances 

Instantiate a minimum of 2 EC2 instances using the following user-data.sh script (available in the files folder):

```
#!/bin/bash
sudo mkdir /home/ec2-user/hello
sudo wget https://scissors-sinners.s3-us-west-1.amazonaws.com/hello.py -P /home/ec2-user/hello
sudo chown -R ec2-user /home/ec2-user/hello
sudo wget https://scissors-sinners.s3-us-west-1.amazonaws.com/hello.service -P /etc/systemd/system
sudo systemctl enable hello; systemctl start hello
```

Also, create a new security group for your EC2 instances named activity_13 and with ingress ports 22 and 8000 opened. When you are done, test accessing the hello app service using the IP address of each EC2 instance. 

### Step 3 - Create a NLB

Choose the following options:

* Load balancer name: activity13
* Network mapping: select all zones in your default VPC
* Listeners and routing: 
    * port 8000
    * create a target group: 
        * target type: instances
        * target group name: activity13
        * port 8000
        * register targets: select the 2 EC2 instances
        * click on include as pending below
    * refresh and select the target group name
    
Wait for the NLB to be provisioned. Then test the hello app now using the LB DNS name. Make sure you are able to see the requests being served by the 2 EC2 instances as your refresh the page. 

### Step 4 - Cleanup 

Don't forget to delete your NLB and the target group.  Also, terminate all EC2 instances that were launched. 
