# Activity 23

## Lambda

## Goal
The goal of this activity is to illustrate how to create a lambda function for a simple python application. 
 
## Steps

### Step 1 - Install virtualenv

Virtualenv is a tool that allows python developers create isolated build environments.  Follow steps in https://virtualenv.pypa.io/en/latest/installation.html to install virtualenv.  

### Step 2 - Create and Activate a Virtual Environment 

```
virtualenv build
cd build
source bin/activate
```

### Step 3 - Install Required Packages 

This python project requires 2 packages: requests and beautifulsoup4. 

```
pip3 install requests
pip3 install beautifulsoup4
```

### Step 4 - Deactivate Virtual Environment

```
deactivate
```

### Step 5 - Package your application with all of its dependencies

Run pip freeze to see all of the dependencies. 

```
beautifulsoup4==4.9.3
certifi==2020.12.5
chardet==4.0.0
idna==2.10
requests==2.25.1
soupsieve==2.2.1
urllib3==1.26.4
```

Copy all of the correspondent library folders, located in lib/python3.9/site-packages, to the build folder (or copy dollar2real.py to the lib folder). Then generate the dollar2real.zip file using the command below:

```
zip -r dollar2real.zip \
    dollar2real.py \
    bs4 \
    certifi \
    chardet \
    idna \
    requests \
    soupsieve \
    urllib3
```

### Step 6 - Create a Lambda Function

* Author from scratch
* Function name: dollar2real
* Runtime: Python 3.6

Click on create function. 

Use "Upload from .zip" to upload the dollar2real.zip file. 

Edit the "Runtime settings" and change the handler of your lambda function to: "dollar2real.lambda_handler".

### Step 7 - Test the Application

Click on the Test tab and then test. Make sure your application runs successfully. You can also run your lambda function from the command line using: 

```
aws lambda invoke --function-name activity23 /dev/stdout
```