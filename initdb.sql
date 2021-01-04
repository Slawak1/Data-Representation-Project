
use datarepresentation

CREATE TABLE users (
  username varchar(45) NOT NULL,
  password varchar(45) NOT NULL,
  name varchar(105) DEFAULT NULL,
  PRIMARY KEY (username)
);

create table customer(
	id int PRIMARY KEY auto_increment,
    name varchar(150),
    phone_no varchar(15),
    email varchar(150)
    );
    
