# Activity 12

## Docker RDS Client (AWS Deploy)

## Goal
The goal of this activity is to recreate the docker container from the previous activity, but this time we want the container to run on AWS. 

## Steps

### Step 1 - Create a Security Group for the ECS Cluster 

Allow access to ports 22 and 80 from anywhere and for the traffic going out. Leave all traffic allowed as the outbound rule for the sg. Name your sg "activity_12". The sg should be create in the default VPC. 

### Step 2 - Create an ECS Cluster 

Choose the following options:

* Template: EC2 Linux + Networking
* Cluster name: activity12
* EC2 instance type: t2.micro
* Number of instances: 1
* Key pair: cs39ab
* VPC: choose your default VPC
* Subnets: just select one for now
* Security group: select activity_12
* Container instance IAM role: ECSInstanceRole

### Step 3 - Create a Task Definition 

Choose the following options:

* Launch type: EC2 
* Task Definition Name: dollar2real
* Task Role: None
* Network Mode: default 
* Task execution IAM role: ecsTaskExecutionRole 
* Container Definitions - Add container:
    * Container name: dollar2real
    * Image: motat/dollar2real (replacing motat with your docker id)
    * Memory Limits (MiB): Hard limit - 128
    * Port mappings: 
        * Host port: 80
        * Container port: 8000
    * Environment variables:
        * DB_HOST: <same used in previous activities>
        * DB_NAME: dollar2real 
        * DB_USER: dollar2real 
        * DB_PASSWORD: 135791

### Step 4 - Create/Test Service 

Go to Clusters - Tasks - Run new Task. The choose the following options:

* Launch type: EC2 
* Task Definition: select dollar2real 
* Service name: dollar2real
* Service type: replica, with only 1 task

To test your service, get your cluster's ECS instance public IP and try to open it using a browser. 