# Activity 11

## Docker w/ RDS + Web Front End

## Goal
The goal of this activity is to recreate the docker container from the previous activity, this time if a web front end. 

## Steps

### Step 1 to 3

Repeat steps from previous activity. 

### Step 4 - Create and Test Application

Copy dollar2real.py from the src folder. Run it to make sure the application is working. Delete the lines that create environment variables once you are satisfied with the db connection and before creating the docker image

### Step 5 - Create Dockerfile

Copy Dockerfile from the src folder to build. 

### Step 6 - Generate Docker Image 

```
docker build -t dollar2real .
```

### Step 7 - Create and Run a Docker Container from Image

Remember to pass the environment variables through the command line. Also, because this time the docker container will be running a TCP service, there is the need to map a port on the host to the container's port. --rm removes the container automatically once it is stopped. 

```
docker run -i --name dollar2real \
    --env DB_HOST=dollar2real.cvhpjdm21h9e.us-west-1.rds.amazonaws.com \
    --env DB_NAME=dollar2real \
    --env DB_USER=dollar2real \
    --env DB_PASSWORD=135791 \
    --publish 8000:8000 \
    --rm \
    dollar2real
```

### Step 8 - Publish Container 

Publish your container on docker hub. 

```
docker tag dollar2real motat/dollar2real
docker push motat/dollar2real
```