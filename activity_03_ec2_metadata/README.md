# Activity 03

## EC2 Instance w/ Metadata

## Goal
The goal of this activity is to launch an EC2 instance and show some of its metadata as an HTML page similar to the following: 

```
Some Metadata Information
ami-id: ami-04468e03c37242e1e
instance-id: i-0803d6ecca91eb255
instance-type: t2.micro
availability-zone: us-west-1c
security-groups: activity_03
```

## Preconditions

Save the ids of the default VPC (eg, vpc-924e57f5) and the public subnet (eg, subnet-b1b256eb). 
 
## Steps

### Step 1 - Create a Security Group 

```
aws ec2 create-security-group \
    --group-name activity_03 \
    --description activity_03 \
    --vpc-id vpc-924e57f5 
```

Save the security group id (eg, sg-0156b96da4a9a8eca).

### Step 2 - Add Ingress Rules to Security Group 

```
aws ec2 authorize-security-group-ingress \
    --group-id sg-0156b96da4a9a8eca \
    --protocol tcp \
    --port 22 \
    --cidr 0.0.0.0/0

aws ec2 authorize-security-group-ingress \
    --group-id sg-0156b96da4a9a8eca \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0    
```

### Step 3 - Define a User Data Script

Save the file below as user-data.sh.

```
#!/bin/bash
yum update -y
yum install httpd -y
systemctl enable httpd
systemctl start httpd
cd /var/www/html
echo "<h2>Some Metadata Information</h2>" > index.html
echo "ami-id: " >> index.html
curl http://169.254.169.254/latest/meta-data/ami-id >> index.html 
echo "<br>" >> index.html 
echo "instance-id: " >> index.html
curl http://169.254.169.254/latest/meta-data/instance-id >> index.html 
echo "<br>" >> index.html
echo "instance-type: " >> index.html
curl http://169.254.169.254/latest/meta-data/instance-type >> index.html 
echo "<br>" >> index.html
echo "availability-zone: " >> index.html
curl http://169.254.169.254/latest/meta-data/placement/availability-zone >> index.html 
echo "<br>" >> index.html
echo "security-groups: " >> index.html
curl http://169.254.169.254/latest/meta-data/security-groups >> index.html 
```

### Step 4 - Launch an EC2 Instance

```
aws ec2 run-instances \
    --image-id ami-04468e03c37242e1e \
    --count 1 \
    --instance-type t2.micro \
    --security-group-ids sg-0156b96da4a9a8eca \
    --subnet-id subnet-b1b256eb \
    --key-name cs39ab \
    --user-data file://user-data.sh
```

Save your instance id (eg i-0a363d90702955db9)

### Step 5 - List all EC2 Instances

```
aws ec2 describe-instances
```

Save the IP address of your instance (eg 54.153.20.13). 

### Step 6 - Connect to your EC2 Instance 

Try openning http://54.153.20.13 using your browser to test if you can see the metadata info as an HTML page. 

### Step 7 - Terminate EC2 Instance 

```
aws ec2 terminate-instances \
    --instance-ids i-0a363d90702955db9
```