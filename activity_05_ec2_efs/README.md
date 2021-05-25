# Activity 05

## EC2 Instances w/ EFS Volume

## Goal
The goal of this activity is to illustrate how an EFS file system can be shared among multiple EC2 instances. 
 
## Steps

### Step 1 - Create an EFS File System

* name should be "data"
* should be placed in the default VPC
* use "one zone"
* write down the name of the AZ 
* write down the security group where the service was placed (which should be in the default sg for the VPC)
* write down the id of the EFS file system for future reference (eg fs-239d743b)

### Step 2 - Create a Security Group 

To simplify configurations, both EC2 instances will be in the same security group, called activity_05.  Other than SSH traffic towards the EC2 instances, this sg should allow all outbout traffic.  Also, update the defaullt sg for the VPC to allow inbound NFS traffic from the activity_05 sg.

### Step 3 - Create EC2 Instances

Create the EC2 instances in the same AZ of the EFS file system. Also, use file/user-data.sh when creating those instances. Finally, make sure to add both instances into the activity_05 sg. 

### Step 4 - Mount EFS File System 

Mount the file system on both EC2 instances using the EFS id. Create a test file and see if it can be accessed from the EC2 instances. 

```
mkdir data
sudo mount -t efs fs-239d743b data
sudo chmod 777 data
```
