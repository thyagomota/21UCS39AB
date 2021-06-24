# Activity 09

## MySQL RDS

## Goal
The goal of this activity is to create an RDS instance running MySQL.  
 
## Steps

### Step 1 - Create RDS Instance

Use the following parameters:

* DB creation method: Standard create
* Engine Type: MySQL
* Version: MySQL 8.0.20
* Templates: Free tier
* DB instance identifier: dollar2real
* Master username: admin
* Master password: <choose your own>
* DB instance class: db.t2.micro
* Connectivity - Public access: yes
* Security group (Create new): dollar2real 
* Availability Zone: <choose your own>

### Step 2 - Connect to MySQL

Use a MySQL client (eg MySQL Workbench) to connect to your database. 

### Step 3 - Create the Database Schema 

Also available under src/dollar2real.sql. 

```
CREATE DATABASE dollar2real;

USE dollar2real;

CREATE TABLE quotes (
  `date`   DATETIME      PRIMARY KEY,
  quote    DECIMAL(8, 4) NOT NULL
);

CREATE USER 'dollar2real' IDENTIFIED BY '135791';

GRANT ALL ON TABLE quotes TO 'dollar2real';
```
