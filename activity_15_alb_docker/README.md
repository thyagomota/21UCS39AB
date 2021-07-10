# Activity 15

## An Application Load Balancer (NLB) w/ Docker Containers

## Goal
This activity is similar to #14. However, instead of using EC2 instances, the application will run on docker containers. 

## Steps

### Step 1 - Build/Test a Docker Image 

Use what you've learned so far to build a docker image for the hello app. Then push your image to docker hub for easy deployment on AWS. Name your image hello. Don't forget to do the port mapping when testing your docker image. 

```
docker run -i --name hello \
    --publish 8000:8000 \
    --rm \
    hello
```

### Step 2 - Create an ECS Cluster, a Task Definition, and a Task

Name your cluster activity 15. Use parameters similar to the ones used in activity 12. 

Because the containers will be running on the same ECS instance, each will need a different port mapping at launching (hosts cannot share ports). Therefore, one of the containers will run on host port 3000 while the other on host port 3001. Make sure to place the ECS cluster in a security group (named activity15) with inbound ports 80, 30000 and 30001 opened. Port 80 will be used later for the ALB. 

After your cluster is provisioned, create 2 task definitions (named taskA and taskB) with the following settings: 

* Launch type: EC2
* Task Definition Name: taskA (then taskB)
* Task Role: None
* Network Mode: default
* Task execution IAM role: ecsTaskExecutionRole
* Container Definitions - Add container:
    * Container name: hello-A
    * Image: motat/hello (replacing motat with your docker id)
    * Memory Limits (MiB): Hard limit - 128
    * Port mappings:
    * Host port: 30000
    * Container port: 8000
* Container Definitions - Add container:
    * Container name: hello-B
    * Image: motat/hello (replacing motat with your docker id)
    * Memory Limits (MiB): Hard limit - 128
    * Port mappings:
    * Host port: 30001
    * Container port: 8000

Now run both tasks based on your hello task definition. Containers hello-A and hello-B should start runninng. Test the containers using the different ECS instance ports. 

The reason we are creting 2 task definitions is to allow us later to stop one of the tasks while keeping the other runninng. 

### Step 3 - Create an ALB

* Name: activity15
* Scheme: internet-facing
* IP address type: Ipv4
* Listener: 80 (that's the port that the LB will be listening to)
* AZs: check all 
* Security Group: activity15
* Target Group: 
    * Name: activity15
    * Port: 3000 (that's one of the ports that the ECS instance listens to)
    * Register Targets: make sure you add the ECS instance on both ports (3000 and 3001)

Test your ALB using its DNS name. Simulate pausing one of the containers (the application should continue to work).
