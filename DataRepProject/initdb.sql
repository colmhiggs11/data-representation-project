DROP DATABASE IF EXISTS datarepresentation;

CREATE DATABASE datarepresentation;

use datarepresentation;

   create table Equipment(
      part_ID int primary key,
      part_name varchar(250),
      checkedInBy varchar(250),
      quantity int)
      ;