# Activity 29

## Use a Lambda Function to Help Implement an Rest API

## Introductionn

Your goal in this activity is to use a lambda function to implement a method in a REST API. REST is a popular choice to implement web service, i.e., a software service that is consumed (used) over the web, allowing applications to exchange data in standard formats, such as JSON or XML, using HTTP (the web transport service). REST stands for “representational state transfer” and is characterized by having web services being implemented using “stateless” operations (or primitives). The term REST was introduced in 2000 by Roy Fielding in his doctoral dissertation.
A RESTful (or REST compliant) web service must comply with the following directives (or good practices for writing scalable REST web services):

* be based on the client-server architecture model;
* the server should not maintain any record or save any context associated with a specific client between multiple;
* client requests (in other words, the server is “stateless”);
* server responses may be cacheable;
* replication transparency (i.e., the client does not need to know that the resource being accessed has been replicated); and
* uniform (same) access using a well-defined API.

The REST API to be implemented in this activity will have a single (GET) method that takes 2 sentences (a and b) and returns the similarity score (from 0 to 1) that tells how similar the 2 sentences are.  

## Steps

### Step 1 - Create the Lambda Function

Use the code in src to create the compute_similarity lambda function. The code requires a module named stemming that computes the stem (the base) of a given word. Therefore, you need to package the function in a zip that contains the required library. We suggest the following zip command to create the package: 

```
zip -r compute_similarity.zip \
    compute_similarity.py \
    stemming
```

Make sure you have the stemming library in your build folder. Before you proceed you should test your lambda function using the following event object: 

```
{ 
    "a": "cheap electronic items", 
    "b": "discount electronics coupon"
}
```

You should get the following return from the lambda function execution (0.2 is the similarity score returned): 

```
{'statusCode': 200, 'body': '0.2'}
```

### Step 2 - Create an API Gateway 

* API type: REST API
* API name: similarity
* Resource Actions - Create Method:
    * choose GET
    * Integration type: Lambda Function
    * Lambda Function: compute_similarity
    * Method Request:
        * URL Query String Parameters: add 2 parameters (a and b), both required
    * Integration Request:
        * Mapping Templates: 
            * Request body passthrough: When there are no templates defined (recommended)
            * Content-type: application/json
            * Use the following template:

```
{
    "a": "$input.params('a')",
    "b": "$input.params('b')"
}
```

### Step 3 - Testing 

Click on TEST (under Method Execution). Use the following as your Query String:

```
a=cheap electronic items&b=discount electronics coupon
```

If it works, click on Actions - Deploy API to get an URL for your API. Give your stage a name (like amazing-api) and hit deploy. Then test your API now using its URL, like: 

https://irt642nkvf.execute-api.us-west-1.amazonaws.com/amazing-api?a=cheap electronic items&b=discount electronics coupon
