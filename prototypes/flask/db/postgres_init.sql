drop user root;
create user root with password 'root';
grant all privileges on all tables in schema public to root;
drop database forsale;
create database forsale;
\c forsale

create table properties(pid int primary key, type varchar(10),status varchar(20), bedrooms int, bathrooms int, area float, cost float, locality varchar(20), address varchar(60) );

create table users( username varchar(30) primary key, passwd varchar(1000), firstname varchar(30), lastname varchar(30), email varchar(30), phone varchar(20) );

create table posts_ad(username varchar(30), pid int FOREIGN KEY REFERENCES properties(pid)
 , date posted_date);

create table purchase(username varchar(30), pid int FOREIGN KEY REFERENCES properties(pid) , date purchased_date);

create table request(username varchar(30), pid int FOREIGN KEY REFERENCES properties(pid) , date requested_date);

create table property_images(prop_id int NOT NULL primary key ,image BLOB);

create table tags(pid int NOT NULL , tag varchar(30), primary key(pid,tag));

create table property_analytics(p_id int NOT NULL primary key AUTO_INCREMENT , distance int);

/* Dummy values */

insert into properties values(1,'Rent','Ready to Move',2,1,1230,1200300,'MurugeshPalya','S R Layout ');
insert into properties values(2,'Buy','Ready to Move',1,2,314,43525245,'MurugeshPalya','Indiranagar ');
insert into properties values(3,'Rent','Ready to Move',3,1,414,2131414,'Ittamadu','Banashankari ');
insert into properties values(4,'Buy','Ready to Move',4,1,1445,4134145,'Hoskerehalli',' Banashankari');
insert into properties values(5,'Rent','Ready to Move',2,2,34513,145531,'MurugeshPalya','R R Nagar');


insert into users values('ram_raj','ram_123','ram','raj','ram.raj@gmail.com','9445245856');
insert into users values('ram_roy','ram_roy','ram','roy','ram.roy@gmail.com','9446585856');
insert into users values('sadvi_s','ssadvi','sadvi','s','sadvis@gmail.com','9427955856');
insert into users values('mani_m','mani_123','mani','m','mmani@gmail.com','9408715856');
insert into users values('rajath','rajath_123','rajath','r','raj.raj@gmail.com','9980155856');


insert into posts_ad values('ram_raj',1,20-06-2000);
insert into posts_ad values('ram_roy',2,10-07-2001);
insert into posts_ad values('rajath',1,10-02-2003);
insert into posts_ad values('mani_m',5,22-06-2007);
insert into posts_ad values('sadvi_s',9,30-01-2012);


insert into purchase values('ram_raj'1,22-07-2012);
insert into purchase values('mani_m'2,23-05-2001);
insert into purchase values('sadvi_s'6,24-06-2002);
insert into purchase values('ram_raj'9,16-03-2007);
insert into purchase values('ram_raj'2,17-04-2009);


insert into request values('mani_m'1,15-07-2013);
insert into request values('ram_raj'2,11-11-2016);
insert into request values('sadvi_s'3,09-12-2009);
insert into request values('rajath'4,23-06-2006);
insert into request values('ram_raj'9,27-02-2005);



insert into property_image values(5,'1.png');
insert into property_image values(7,'2.png');
insert into property_image values(9,'3.png');
insert into property_image values(1,'4.png');
insert into property_image values(2,'5.png');

insert into tags values(1,'Swimming Pool');
insert into tags values(1,'Gym');
insert into tags values(2,'Restaurant');
insert into tags values(3,'Play House');
insert into tags values(3,'Buffet House');
insert into tags values(3,'Gym');
insert into tags values(4,'Lounge');
insert into tags values(4,'Swimming Pool');
insert into tags values(5,'Gym');


insert into property_analytics values(1,4);
insert into property_analytics values(2,9);
insert into property_analytics values(3,7);
insert into property_analytics values(4,2);
insert into property_analytics values(5,1);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO root;