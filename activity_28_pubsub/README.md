# Activity 28

## Simulate the Publish-Subscribe Communication Pattern

## Goal

Your goal in this activity is to simulate the publish-subscribe communication pattern using AWS SNS and Lambda services. You will create two publishers, one for a bees-related topic, and another one for Colorado-related topic. Then you will configure two subscribers: John will only be interested in the bees topic, while Mary will be subscribing both topics (bees and Colorado). 

## Steps

### Step 1 - Create the Topics

Using SNS (Simple Notification Service), create the bees and the colorado topics, both based of the standard type. 

### Step 2 - Create Policies and Roles 

Create the BeesTopicFullAccess and the ColoradoTopicFullAccess policies giving full access privileges to the bees and colorado topics, respectively. Then, create the BeesPublisherRole and ColoradoPublisherRole, attaching the AWSLambda_FullAccess (AWS managed) policy to both roles, and then the BeesTopicFullAccess and ColoradoTopicFullAccess policies to the BeesPublisherRole and ColoradoPublisherRole, respectively. 

### Step 3 - Create the Publisher Lambda Functions 

Use the provided code to create the bees_publisher and the colorado_publisher lambda functions.  Each function shoulld have an environment variable called TOPIC_ARN, which points to the correct topic arn. Also, they should have the correct role: BeesPublisherRole or ColoradoPublisherRole. Make sure both functions work as expected. 

### Step 4 - Create the Subscriber Lambda Functions

Use the provided code to create the john_subscriber and the mary_subscriber lambda functions.  Once the functions are deployed, go to each topic configuration screen and have john_subscriber function subscribe to the bees topics and mary_subscriber function subscribe to both topics. 

### Step 5 - Testing 

Leave cloudwatch monitors of each function open on different tabs. Using bees_publisher, send a message. Then using colorado_publisher, send another message. John should receive the event notification for the bees messaage, while mary should receive the notification for both messsages sent: bees and colorado. 
