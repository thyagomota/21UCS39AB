# Lab 01

## Setup a WordPress Blog Server

## Goal
The goal of this project is for you to setup a WordPress blog server on AWS.  WordPress is a free and open-source content management system written in PHP with built-in support for MySQL/MariaDB databases.  Because your solution should allow full control over the blog web server, you are required to configure an EC2 instance built from scratch.   
 
## Instructions

The bulk of the instructions for this lab are available online at [Tutorial: Host a WordPress blog on Amazon Linux 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hosting-wordpress.html). However, your solution must meet a few   requirements (described next). 

### Requirement #1 - VPC & Subnet 

* Your WordPress blog server should be created in the public sunet of the default VPC of a region (e.g., us-west-1). 

### Requirement #2 - LAMP Stack & EC2 Instance 

* The LAMP (Linux Apache MySQL PHP) stack must be installed and configured automatically using a user-data.sh script. 
* The EC2 instance hosting the LAMP stack should be configured and launched automatically using a Python script named lab01.py. 
* Also, the EC2 instance should be placed in a security group named lab01, with inbound ssh (port 22), http (port 80), and mysql/mariadb (port 3306) traffic enabled from anywhere. 
* Your Python script should display the public IP of the EC2 instance before it finishes. 

Checkpoint: openning the IP address on a browser should display Apache's test page. 

### Requirement #3 - Database Configuration

You should secure your mysql/mariadb database configuration according to the instructions described in the tutorial. After that, run the following db configurations command on your EC2 instance (change the password if you want to):

```
CREATE USER 'wordpress-user'@'localhost' IDENTIFIED BY '135791';
CREATE DATABASE `wordpress-db`;
GRANT ALL PRIVILEGES ON `wordpress-db`.* TO "wordpress-user"@"localhost";
FLUSH PRIVILEGES;
```

### Requirement #4 - WordPress Setup 

Run the following commands to download and install WordPress: 

```
wget "https://wordpress.org/latest.tar.gz"
tar -xzf latest.tar.gz
cp wordpress/wp-config-sample.php wordpress/wp-config.php
```

When you are done, finish WordPress setup following the steps described in [Tutorial: Host a WordPress blog on Amazon Linux 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hosting-wordpress.html), including:

* edit wp-config.php file with the db configurations;  
* copy wordpress folder to apache; 
* allow wordpress to use permalinks in apache;  
* install PHP graphics drawing library (optional); and 
* fix file permissions on apache.

### Requirement #5 - AMI Generation

Before running the WordPress installation script on a browser, create an AMI (Amazon Machine Image) named lab01 from your EC2 instance. Search online how to generate an AMI from an EC2 instance. After you generate your AMI, try to run a new WordPress server from it. 

Once you are satisfied with your AMI, share it with your instructor (AWS Account Number 939096940193) for grading purposes. See instructions on how to share an AMI image with another account [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html). 

### Requirement #5 - WordPress Blog Server Fully Functional

Open the blog server using http://<IP>/wp-config.php

## Deliverables 

* A zip file named lab01.zip containing your user-data.sh and the lab01.py Python script. 
* In the comments section of lab01.py you should write the names of the team members and the IP address of your WordPress server so your instructor can access it remotely. 
* In addition, the instructor should be able to launch an EC2 instance using the AMI that you shared previously. 

## Rubric

* \+30 user-data.sh 
    * \+5 packages are updated
    * \+10 lamp stack installed
    * \+5 apache setup
    * \+5 db setup
    * \+5 wp setup
* \+45 lab01.py
    * \+15 security group 
    * \+20 EC2 instance launched automatically and configured using user data
    * \+10 public IP is displayed at the end
* \+15 WordPress Server AMI shared with instuctor
* \+10 WordPress is fully functional
* \-5 team members are not identified 
* \-5 zip format wasn't used