# Activity 08

## Docker Image Build

## Goal
The goal of this activity is to illustrate how to create a docker image for a python application. 
 
## Steps

### Step 1 - Install virtualenv

Virtualenv is a tool that allows python developers create isolated build environments.  Follow steps in https://virtualenv.pypa.io/en/latest/installation.html to install virtualenv.  

### Step 2 - Create and Activate a Virtual Environment 

```
virtualenv build
cd build
source bin/activate
```

### Step 3 - Create Public Subnet

Name it "pub" and use 192.168.10.0/24 as CIDR block. After the subnet is created, modify auto-assign IP, enabling it. 

### Step 4 - Install Required Packages 

This python project requires 2 packages: requests and beautifulsoup4. 

```
pip3 install requests
pip3 install beautifulsoup4
```

### Step 5 - Generate Requirements Text File

```
pip3 freeze > requirements.txt
```

### Step 6 - Create and Test Application

Copy dollar2real.py from the src folder. Run it to make sure the application is working. 

When you VPC was created, a route table was automatically created with one default local route.  Associate this route table to the public subnet and create a default route redirecting traffic to the internet gateway. 

### Step 7 - Create Dockerfile

Copy Dockerfile from the src folder. 

### Step 8 - Generate Docker Image 

```
docker build -t dollar2real .
```

### Step 9 - Create and Run a Docker Container from Imagee

```
docker run -i --name dollar2real dollar2real
```

### Step 10 - Delete Docker Container 

```
docker rm dollar2real
```