# Homework 02

## EC2 Instance w/ EFS Volume

## Goal
The goal of this assignment is for you to describe the command-line interface (CLI) commands required to create an EFS file system to be shared among two EC2 instances. 

## TODO #1 - Create an EFS File System

* name should be "data"
* should us "general purpose" performance mode
* use the "one zone" option
* hint: use efs's "create-file-system" command

```
YOUR ANSWER HERE
```

Write down the id of the EFS file system returned by the command. 

```
EFS file system id: YOUR ANSWER HERE
```

## TODO #2 - Create a Mount Target 

This command is used to specify which subnet will be used to mount the efs share. 

* hint: use efs's "create-mount-target" command

You will need the subnet ID. 

```
YOUR ANSWER HERE
```

## TODO #3 - Create a Security Group

* name should be "homework_02"
* it should allow ssh (ingress) traffic from anywhere 
* it should use the default VPC

```
YOUR ANSWER HERE
```
Write down the id of the EFS file system returned by the command. 

```
Security group id: YOUR ANSWER HERE
```

```
YOUR ANSWER HERE
```

## TODO #4 - Create Ingress Rule in Default Security Group

* add an ingress rule allowing NFS traffic comming from homework_02 security group. 

```
YOUR ANSWER HERE
```

## TODO #5 Define a User Data Script

Save the file below as user-data.sh.

```
#!/bin/bash
yum update -y
yum install -y amazon-efs-utils
```

## TODO #6 Launch 2 EC2 Instances 

* they should be in the homework_02 security group
* make sure they are launched in the default VPC's public subnet 
* they should use user-data.sh

```
YOUR ANSWER HERE
```

## Final Test 

If all steps were done correctly, you should be able to mount the EFS file system in both EC2 instances. 

```
mkdir data
sudo mount -t efs fs-7ef80d66 data
```

## Deliverable

Upload to canvas this README.md file containing all of the steps. 