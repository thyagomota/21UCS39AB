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