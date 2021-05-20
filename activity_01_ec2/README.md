# Activity 01

## Launching an EC2 Instance on a Public Subnet

## Goal
This goal of this activity is to describe the steps needed to launch an EC2 instance on a public subnet. 
 
## Steps

### Step 1 - List VPCs

```
aws ec2 describe-vpcs
```

Save the id of the default VPC (eg, vpc-924e57f5). Also, can you tell what's the CIDR block of your default VPC?

### Step 2 - List the Subnets of the Default VPC

```
aws ec2 describe-subnets \
    --filters "Name=vpc-id,Values=vpc-924e57f5"
```

Save the id of the subnet that has the property MapPublicIpOnLaunch set to true (eg, subnet-b1b256eb). 

### Step 3 - Create a Security Group 

```
aws ec2 create-security-group \
    --group-name activity_01 \
    --description activity_01 \
    --vpc-id vpc-924e57f5 
```

Save the security group id (eg, sg-093ec88542bd9d8ab).

### Step 4 - Add an Ingress Rule to Security Group 

```
aws ec2 authorize-security-group-ingress \
    --group-id sg-093ec88542bd9d8ab \
    --protocol tcp \
    --port 22 \
    --cidr 0.0.0.0/0
```

### Step 5 - Launch an EC2 Instance

```
aws ec2 run-instances \
    --image-id ami-04468e03c37242e1e \
    --count 1 \
    --instance-type t2.micro \
    --security-group-ids sg-093ec88542bd9d8ab \
    --subnet-id subnet-b1b256eb \
    --key-name cs39ab
```

Save your instance id (eg i-03b47cff33c01f997)

### Step 6 - List all EC2 Instances

```
aws ec2 describe-instances
```

Save the IP address of your instance (eg 54.176.8.107). 

### Step 7 - Connect to your EC2 Instance 

```
ssh -i cs39ab.pem ec2-user@54.176.8.107
```

### Step 8 - Terminate EC2 Instance 

```
aws ec2 terminate-instances \
    --instance-ids i-03b47cff33c01f997
```