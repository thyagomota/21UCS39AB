# Activity 02

## Launch an EC2 Instance w/ Apache Server

## Goal
The goal of this activity is to describe the steps needed to start an Apache server on an EC2 instance for public access. 

## Preconditions

Save the ids of the default VPC (eg, vpc-924e57f5) and the public subnet (eg, subnet-b1b256eb). 
 
## Steps

### Step 1 - Create a Security Group 

```
aws ec2 create-security-group \
    --group-name activity_02 \
    --description activity_02 \
    --vpc-id vpc-924e57f5 
```

Save the security group id (eg, sg-0156b96da4a9a8eca).

### Step 1 - Add Ingress Rules to Security Group 

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
echo "This is INSTANCE ${HOSTNAME}" > index.html
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

```
ssh -i cs39ab.pem ec2-user@54.153.20.13
```

Also, try to open http://54.153.20.13 using your browser to test if Apache is up and running. 

### Step 7 - Terminate EC2 Instance 

```
aws ec2 terminate-instances \
    --instance-ids i-0a363d90702955db9
```