# Activity 04

## EC2 Instance w/ EBS Volume

## Goal
The goal of this activity is to create an EBS volume and attach/mount it to an EC2 instance. 

## Preconditions

Save the id of an EC2 instance (eg i-0c12f821c68a5f301) launched in a public subnet and accessible through ssh. Also, make sure to write down the availability zone (eg us-west-1c) where you EC2 instance was created. 
 
## Steps

### Step 1 - Create an EBS Volume

```
aws ec2 create-volume \
    --availability-zone us-west-1c \
    --volume-type gp2 \
    --size 1 
```

Save the volume id (eg, vol-0bc19f6a34df4a8fe).

### Step 2 - Attach the EBS Volume to the EC2 Instance 

```
aws ec2 attach-volume \
    --device /dev/sdb \
    --instance-id i-0c12f821c68a5f301 \
    --volume-id vol-0bc19f6a34df4a8fe    
```

### Step 3 - Connect to your EC2 Instance and Mount the Volume

```
sudo mkdir /data
sudo mkfs -t xfs /dev/sdb 
sudo mount /dev/sdb /data
sudo chmod 777 /data
```

Try creating a file in /data. 

### Step 4 - Terminate EC2 Instance 

```
aws ec2 terminate-instances \
    --instance-ids i-0c12f821c68a5f301
```