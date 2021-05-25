CREATE DATABASE dollar2real;

USE dollar2real;

CREATE TABLE quotes (
  `datetime` DATETIME      PRIMARY KEY,
  quote      DECIMAL(8, 4) NOT NULL
);

CREATE USER 'dollar2real' IDENTIFIED BY '135791';

GRANT ALL ON TABLE quotes TO 'dollar2real';


