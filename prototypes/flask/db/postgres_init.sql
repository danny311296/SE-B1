drop user root;
create user root with password 'root';
grant all privileges on all tables in schema public to root;
drop database forsale;
create database forsale;
\c forsale

create table users( username varchar(30) primary key, passwd varchar(1000), firstname varchar(30), lastname varchar(30), email varchar(30), phone varchar(20) );

create table properties(pid int primary key, type varchar(10),status varchar(20), bedrooms int, bathrooms int, area float, cost float, locality varchar(20), address varchar(60) );

create table tags(pid int, tag varchar(30), primary key(pid,tag));

/* Dummy values */

insert into properties values(1,'Rent','Ready to Move',2,1,1230,1200300,'MurugeshPalya','S R Layout ');
insert into properties values(2,'Buy','Ready to Move',1,2,314,43525245,'MurugeshPalya','S R Layout ');
insert into properties values(3,'Rent','Ready to Move',3,1,414,2131414,'MurugeshPalya','S R Layout ');
insert into properties values(4,'Buy','Ready to Move',4,1,1445,4134145,'MurugeshPalya','S R Layout ');
insert into properties values(5,'Rent','Ready to Move',2,2,34513,145531,'MurugeshPalya','S R Layout ');

insert into tags values(1,'Swimming Pool');
insert into tags values(1,'Gym');
insert into tags values(2,'Restaurant');
insert into tags values(3,'Play House');
insert into tags values(3,'Buffet House');
insert into tags values(3,'Gym');
insert into tags values(4,'Lounge');
insert into tags values(4,'Swimming Pool');
insert into tags values(5,'Gym');

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO root;