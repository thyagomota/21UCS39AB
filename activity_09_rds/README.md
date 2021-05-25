# Activity 09

## MySQL RDS Setup

## Goal
The goal of this activity is to create an RDS instance running MySQL.  
 
## Steps

### Step 1 - Create RDS Instance

Use the following parameters:

* DB creation method: Standard create
* Engine Type: MySQL
* Version: MySQL 8.0.20
* Templates: Free tier
* DB instance identifier: seamagnet
* Master username: admin
* Master password: <choose your own>
* DB instance class: db.t2.micro
* Connectivity - Public access: yes
* Security group (Create new): seamagnet 
* Availability Zone: <choose your own>

### Step 2 - Connect to MySQL

Use a MySQL client (eg MySQL Workbench) to connect to your database. 

### Step 3 - Create the Database Schema 

Also available under src/seamagnet.sql. 

```
CREATE DATABASE seamagnet;

USE seamagnet;

CREATE TABLE Departments (
  code   CHAR(2)     PRIMARY KEY,
  `desc` VARCHAR(25) NOT NULL
);

INSERT INTO Departments VALUES ( 'HR', 'Human Resources' );
INSERT INTO Departments VALUES ( 'IT', 'Information Technology' );
INSERT INTO Departments VALUES ( 'SL', 'Sales' );

CREATE TABLE Employees (
  id       INT         AUTO_INCREMENT PRIMARY KEY,
  name     VARCHAR(30) NOT NULL,
  sal      INT         NOT NULL,
  deptCode CHAR(2),
  FOREIGN KEY (deptCode) REFERENCES Departments (code)
);

INSERT INTO Employees (name, sal, deptCode) VALUES ('Sam Mai Tai',        50000,  'HR');
INSERT INTO Employees (name, sal, deptCode) VALUES ('James Brandy',       55000,  'HR');
INSERT INTO Employees (name, sal, deptCode) VALUES ('Whisky Strauss',     60000,  'HR');
INSERT INTO Employees (name, sal, deptCode) VALUES ('Romeo Curacau',      65000,  'IT');
INSERT INTO Employees (name, sal, deptCode) VALUES ('Jose Caipirinha',    65000,  'IT');
INSERT INTO Employees (name, sal, deptCode) VALUES ('Tony Gin and Tonic', 80000,  'SL');
INSERT INTO Employees (name, sal, deptCode) VALUES ('Debby Derby',        85000,  'SL');
INSERT INTO Employees (name, sal, deptCode) VALUES ('Morbid Mojito',      150000, NULL);
```
