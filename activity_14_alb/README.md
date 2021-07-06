# Activity 14

## An Application Load Balancer (ALB)

## Goal
The goal of this activity is to illustrate how to create an Application Load Balancer (ALB) in AWS. 

## Steps

### Step 1 - Create an S3 Bucket 

Same as activity 13. 

### Step 2 - Instantiate EC2 Instances 

Same as activity 13.  

### Step 3 - Create an ALB

Use options similar to the ones used in activity 13. 
    
Wait for the ALB to be provisioned. Then test the hello app now using the LB DNS name. Make sure you are able to see the requests being served by the 2 EC2 instances as your refresh the page. Stop one of the instances if needed. 

### Step 4 - Cleanup 

Don't forget to delete your ALB and the target group.  Also, terminate all EC2 instances that were launched. 
