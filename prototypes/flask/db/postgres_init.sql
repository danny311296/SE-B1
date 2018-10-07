drop user root;
create user root with password 'root';
grant all privileges on all tables in schema public to root;
drop database forsale;
create database forsale;
\c forsale

create table users(username varchar(30) primary key, passwd varchar(30), firstname varchar(30), lastname varchar(30), email varchar(30),phone varchar(20) );

insert into users values('dan32039','asdefef','Danv','adcd','abc@abc.com','9902922932');