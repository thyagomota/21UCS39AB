# Lab 03

## The Ethereum Microservice Webapp

## Goal
Write an microservice webapp that consists of the 2 lambda functions described next. 

### Ethereum Scrape (backend)

This function should scrape ethereum price from [https://www.coindesk.com/price/ethereum](https://www.coindesk.com/price/ethereum), inserting the date, time, and price on a MySQL database running on RDS.  The scrape function should run on a schedule, getting the ethereum price once a day. 

### Ethereum Display (frontend)

This function should display all ethereum prices collected using an HTML page (similar to the following). 

![lab03](images/lab03.png)

The ethereum display function should be called from an ALB. 

### Requirements 

Both functions should be called automatically by triggers. The db parameters should be configured using environment variables. 

## Deliverables 

* ethereum_scrape.py (the scrape function)
* ethereum_display.py (the display function)
* ethereum.sql (SQL script that creates the database)

Zip all of the files and submit the zip on Canvas. 

In addition to those deliverables, you should also write a comment (on Canvas) with the URL of you webapp so I can test it remotely. I will try to grade as soon as possible and let you know when I am done so you can shutdown services. 

## Rubric

* \+10 sql script
* \+30 scrape function
* \+30 display function
* \+20 triggers (\+10 each)
* \+10 alb
* \-5 team members are not identified 
* \-5 zip format wasn't used