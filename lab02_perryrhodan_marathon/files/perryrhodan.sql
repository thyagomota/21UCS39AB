CREATE DATABASE perryrhodan;

USE perryrhodan;

CREATE TABLE registrations (
  email  VARCHAR(50) PRIMARY KEY,
  first  VARCHAR(30) NOT NULL, 
  last   VARCHAR(30) NOT NULL, 
  birth  DATE        NOT NULL, 
  event  INT         NOT NULL, 
  time   VARCHAR(30) NOT NULL
);

CREATE USER 'perryrhodan' IDENTIFIED BY '135791';

GRANT ALL ON TABLE registrations TO 'perryrhodan';