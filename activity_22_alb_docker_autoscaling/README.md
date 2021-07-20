# Activity 22

## An ALB w/ Docker Containers + Dynamic Port Mapping + Auto Scaling

## Instructions

In the previous activity we learned that auto scaling can automatically launch EC2 instances and register targets. Can we use the same idea to automatically launch containers in an ECS instance to respond to an increase in traffic? Let's find out!

### Step 1 - Create a Target Group 

Do NOT register any targets. 

### Step 2 - Create an ALB 

Name it activity22, also creating a security group (activity22) with ports 22, 80 and the range 32768-65535 (ephemeral ports used for dynamic ports) openeds. 

### Step 3 - Create an ECS Cluster

Name it activity22 and add TWO ECS instances. Make sure to select the key pair (cs39ab). Note that in this scenario you don't use "launch configuration" or "launch template".  When you create you cluster. Instead, you tell AWS the parameters of each ECS instance. Select all subnets from your default VPC, auto-assign public IP (enabled), and place the instance in the security group activity 22 (created earlier). 

### Step 4 - Create a Task Definition

Create a task definition named activity22 using 0 (zero) as the host port (so we can have dynamic port mapping). 

### Step 5 - Create a Service

* Launch type: EC2
* Task definition: activity22
* Service name: activity22
* Number of tasks: 10
* Task placement: leave it "AZ Balanced Spread"
* Load balancing: connect your service to the activity22 ALB created earlier 
    * Production listener port: 80 (that's the port that the users will use to access the hello app)
    * Target group name: activity22 (the one created earlier)
* Set Auto Scaling:
    * Minimum number of tasks: 4
    * Desired number of tasks: 10
    * Maximum number of tasks: 16 
    * Scaling policy type: Target tracking
        * Policy name: activity22
        * ECS service metric: ALBRequestCountPerTarget
        * Target value: 1,000

## Testing 

Monitor your cluster and wait for an ECS instance to be launched. When I launched my service I had 10 tasks running, each ECS instance with 5 tasks. But remember, we can go up to 16 (with auto scaling). To test the auto scaling, simulate request to your web app using the stress script (under src). Try it with 10 threads sending requests every 1/2s. Monitor the #requests received by your load balancer. When it passes 1,000 you should be able to see more tasks being addedd to your cluster. I was able to have my cluster go from 10 tasks to 14 tasks with the parameters described here. 
