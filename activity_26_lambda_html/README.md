# Activity 26

## Lambda w/ HTML output

## Goal
Can a lambda function produce a dynamically generated HTML content to be displayed by a client using a browser? This is a very common scenario as lambda function can be used to implement microservices-based web apps. 
 
## Steps

### Step 1 - Create the Greetings Lambda Function

Use the code in src to create the greetings lambda function. 

### Step 2 - Create a Target Group

Name it activity26 and select "Lambda function" as the target type. Then select the greetings lambda function on the next page. 

### Step 3 - Create an ALB

Name it activity26 and use the target group created previously. The moment you create an ALB having a lambda function as target, a new ALB trigger is added automatically to your lambda function. From now on your lambda function will be invoked by the ALB whenever there is a request from clients.  