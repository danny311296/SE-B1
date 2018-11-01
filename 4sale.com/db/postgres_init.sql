drop user root;
create user root with password 'root';
grant all privileges on all tables in schema public to root;
drop database forsale;
create database forsale;
\c forsale

create table properties(pid serial primary key, title varchar(100), locality varchar(30), type varchar(10), short_description varchar(100), description varchar(1000), bedrooms int, bathrooms int, patio int, address varchar(30), city varchar(20), pincode int, cost float, area float, latitude float, longitude float);

create table users( username varchar(30) primary key, passwd varchar(1000), firstname varchar(30), lastname varchar(30), email varchar(30), phone varchar(20) );

create table posts_ad(username varchar(30), pid int, posted_date date, primary key(username,pid), FOREIGN KEY(pid) REFERENCES properties(pid), FOREIGN KEY(username) REFERENCES users(username));

create table purchase(username varchar(30), pid int, purchased_date date, primary key(pid), FOREIGN KEY(pid) REFERENCES properties(pid), FOREIGN KEY(username) REFERENCES users(username));

create table request(username varchar(30), pid int, requested_date date, primary key(username,pid), FOREIGN KEY(pid) REFERENCES properties(pid), FOREIGN KEY(username) REFERENCES users(username));

create table property_images(pid int, image varchar(30), primary key(pid,image));/*, FOREIGN KEY(pid) REFERENCES properties(pid));*/

create table tags(pid int, tag varchar(30), primary key(pid,tag), FOREIGN KEY(pid) REFERENCES properties(pid));

create table property_analytics(pid int NOT NULL primary key , hospital1 varchar(100), hospital2 varchar(100), bank1  varchar(100), bank2  varchar(100), book_store1 varchar(100), book_store2  varchar(100), bus_station1 varchar(100), bus_station2 varchar(100), school1 varchar(100), school2 varchar(100), clothing_store1 varchar(100), clothing_store2 varchar(100), restaurant1 varchar(100), restaurant2 varchar(100), gym1 varchar(100), gym2 varchar(100), gas_station1 varchar(100), gas_station2 varchar(100), doctor1 varchar(100), doctor2 varchar(100), electronics_store1 varchar(100), electronics_store2 varchar(100), pharmacy1 varchar(100), pharmacy2 varchar(100), green_cover float);

create table complaints(ward varchar(30),complaint varchar(1000));

create table ward_mapping(locality varchar(60),ward varchar(60));

/* Dummy values */
/*
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area, latitude, longitude) values('Beautiful Green House','Murugeshpalya','Sale','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',2,1,1,'12 S R Layout','Bangalore',560017,120300,3020,12.95100100,77.6100510);
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area, latitude, longitude) values('Beautiful Blue House','Murugeshpalya','Sale','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',1,2,1,'12 S R Layout','Bangalore',560017,120300,3020,12.95100100,77.6100510);
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area, latitude, longitude) values('House for sale','Murugeshpalya','Sale','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',2,1,1,'12 S R Layout','Bangalore',560017,120300,3020,12.95100100,77.6100510);
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area, latitude, longitude) values('Villa in domlur','Murugeshpalya','Sale','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',2,1,1,'12 S R Layout','Bangalore',560017,120300,3020,12.95100100,77.6100510);
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area, latitude, longitude) values('Green Villa','Murugeshpalya','Rent','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',2,1,1,'12 S R Layout','Bangalore',560017,120300,3020,12.95100100,77.6100510);
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area, latitude, longitude) values('Green Bungalow','Murugeshpalya','Sale','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',2,1,1,'12 S R Layout','Bangalore',560017,120300,3020,12.95100100,77.6100510);

insert into users values('ram_raj','ram_123','ram','raj','ram.raj@gmail.com','9445245856');
insert into users values('ram_roy','ram_roy','ram','roy','ram.roy@gmail.com','9446585856');
insert into users values('sadvi_s','ssadvi','sadvi','s','sadvis@gmail.com','9427955856');
insert into users values('mani_m','mani_123','mani','m','mmani@gmail.com','9408715856');
insert into users values('rajath','rajath_123','rajath','r','raj.raj@gmail.com','9980155856');


insert into posts_ad values('ram_raj',1,'2000-02-01');
insert into posts_ad values('ram_roy',2,'2001-02-03');
insert into posts_ad values('rajath',1,'2001-02-03');
insert into posts_ad values('mani_m',5,'2001-02-03');
insert into posts_ad values('sadvi_s',3,'2001-02-03');


insert into purchase values('ram_raj',1,'2001-02-03');
insert into purchase values('mani_m',2,'2001-02-03');
insert into purchase values('sadvi_s',3,'2001-02-03');
insert into purchase values('ram_raj',4,'2001-02-03');
insert into purchase values('ram_raj',5,'2001-02-03');


insert into request values('mani_m',1,'2001-02-03');
insert into request values('ram_raj',2,'2001-02-03');
insert into request values('sadvi_s',3,'2001-02-03');
insert into request values('rajath',4,'2001-02-03');
insert into request values('ram_raj',3,'2001-02-03');

insert into property_images values(5,'1.png');
insert into property_images values(3,'2.png');
insert into property_images values(2,'3.png');
insert into property_images values(1,'4.png');
insert into property_images values(2,'5.png');

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
*/
\copy complaints from 'input_csv_files/complaints.csv' DELIMITER ',' CSV

\copy ward_mapping from 'input_csv_files/ward-mapping.csv' DELIMITER ',' CSV

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO root;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO root;