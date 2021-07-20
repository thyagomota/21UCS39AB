# Activity 16

## An Application Load Balancer (ALB) w/ Docker Containers + Dynamic Port Mapping

## Goal
This activity builds from activity 15 by creating a service that automatically launches 10 (container) tasks for the hello app. For that to be manageable, we will be using a feature called dynamic port mapping.  

## Instructions
Remember that in activity 15 we had to manually register the target containers because they were bound to different ports of the ECS instance. But what if our application requires a large number of ECS instances and containers in order to scale properly. Manually registering targets become unfesabible. 

Using a feature called dynamic port mapping, you can configure your load balancer to register targets automatically.  This is done by creating a task definition using 0 (zero) as the host port. By doing so, AWS will interpreter that you want the ECS instance to automatically pick a host port that is available every time it needs to launch a task (ie, a container). Also, when creating your load balancer, make sure to skip the target registration (as this will be done automatically) by a cluster service. 

## Steps

Because this activity requires many steps, we will be doing it in class togoether. This [link](https://faun.pub/understanding-dynamic-port-mapping-in-amazon-ecs-with-application-load-balancer-bf705ee0ca8e) by Mohit Shrestha can be used for future references if you miss one of the steps or need more explanation.  

## Cleanup

Don't forget to delete your service and stop all tasks. Then delete your cluster and load balancer.  