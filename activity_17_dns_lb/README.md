# Activity 17

## A DNS-based LB using a Weighted Routing Policy

## Goal
The goal of this activity is to illustrate how to reproduce a load balancing functionality using a DNS weighted routing policy. Unfortunately, to reproduce this activity you will need to register a domain (which costs $12/year).  If you don't want to register a domain, just follow along and make sure you understand all steps demonstrated by your instructor. 

## Steps

Use the same configuration (steps 1 & 2) of Activity #14. Make sure that you can access the application from both instances before proceeding. 

### Step 3 - Create a Weighted Routing Policy

All of the steps are created in a hosted zone and through Route 53. 

* Create record
* Select "switch to wizard"
* Choose "Weighted Routing Policy"
    * Record name: hello
    * Weighted records to add to "your domain":
        * Value/Route traffic to: "IP address or another value, depending on the record type"
        * In the text area below, enter the (public) IP address of one of the EC2 instances
        * Weight: 50
        * Record ID: helloA
        * repeat the step for the other EC2 instance (use the same weight and helloB for the record ID)

Test your application using the DNS-based load balancer. 

If you are a Mac user, use the following command to clear your local DNS cache. 

```
dscacheutil -flushcache 
```

To send a DNS name resolution request, use the "dig" command like: 

```
dig hello.thyagomota.com
```

### Step 4 - Cleanup 

Don't forget to delete any DNS records created.  Also, terminate all EC2 instances that were launched. 
