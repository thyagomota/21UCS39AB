# Activity 24

## Lambda

## Goal
The goal of this activity is to illustrate how to create a lambda function for a python application running on a schedule. 
 
## Steps

### Step 1 - Package the Application

Use what you've learned so far about packaging Python apps with dependency libraries. 

```
zip -r dollar2real.zip \
    dollar2real.py \
    bs4 \
    certifi \
    chardet \
    idna \
    requests \
    soupsieve \
    urllib3 \
    mysql \
    mysqlx
```

### Step 2 - Create a Lambda Function

Use what you've learned to create a lambda function named dollar2real. Also, configure environment variables accordingly. 

### Step 3 - Test the Application

Click on the Test tab and then test. Make sure your application runs successfully. Then add the following trigger: 

* EventBridge (CloudWatch Events)
* Create a new rule: 
    * Rule name: run_every_5m
    * Rule type: schedule expression
    * Schedule expression: cron(0/5 * * * ? *)

Make sure to remove the trigger after you test your application so you don't incurr in costs. 