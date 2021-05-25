# Activity 10

## Docker w/ RDS

## Goal
The goal of this activity is to create a docker container that connects to and uses a MySQL database running as an RDS instance. 

## Steps

### Step 1 - Create and Activate a Virtual Environment 

```
virtualenv build
cd build
source bin/activate
```

### Step 2 - Install Required Packages 

This python project requires 3 packages: requests, beautifulsoup4, and mysql-connector-python. 

```
pip3 install requests
pip3 install beautifulsoup4
pip3 install mysql-connector-python
```

### Step 3 - Generate Requirements Text File

```
pip3 freeze > requirements.txt
```

### Step 4 - Create and Test Application

Copy dollar2real.py from the src folder. Run it to make sure the application is working. Delete the lines that create environment variables once you are satisfied with the db connection and before creating the docker image

### Step 5 - Create Dockerfile

Copy Dockerfile from the src folder to build. 

### Step 6 - Generate Docker Image 

```
docker build -t dollar2real .
```

### Step 7 - Create and Run a Docker Container from Image

```
docker run -i --name dollar2real dollar2real
```

### Step 8 - Delete Docker Container 

```
docker rm dollar2real
```

### Step 9 - Try a Slightly Different Setup

The image created in this activity had the db credentials saved as environment variables inside the docker image.  This setup is not ideal if you envision sharing the image in public repositories, such as docker hub.  Modify your dockerfile by removing the lines that created the environment variables. Then, pass the environment variables through docker run using the --env parameter. 

Once you have secured your image, use the following commands to copy it to docker hub (replace motat with your id in docker). 

```
docker tag dollar2real motat/dollar2real
docker push motat/dollar2real
```