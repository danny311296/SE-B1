drop user root;
create user root with password 'root';
grant all privileges on all tables in schema public to root;
drop database forsale;
create database forsale;
\c forsale

create table properties(pid serial primary key, title varchar(30), locality varchar(30), type varchar(10), short_description varchar(100), description varchar(1000), bedrooms int, bathrooms int, patio int, address varchar(30), city varchar(20), pincode int, cost float, area float);

create table users( username varchar(30) primary key, passwd varchar(1000), firstname varchar(30), lastname varchar(30), email varchar(30), phone varchar(20) );

create table posts_ad(username varchar(30), pid int, posted_date date, primary key(username,pid), FOREIGN KEY(pid) REFERENCES properties(pid), FOREIGN KEY(username) REFERENCES users(username));

create table purchase(username varchar(30), pid int, purchased_date date, primary key(pid), FOREIGN KEY(pid) REFERENCES properties(pid), FOREIGN KEY(username) REFERENCES users(username));

create table request(username varchar(30), pid int, requested_date date, primary key(username,pid), FOREIGN KEY(pid) REFERENCES properties(pid), FOREIGN KEY(username) REFERENCES users(username));

create table property_images(pid int, image varchar(30), primary key(pid,image), FOREIGN KEY(pid) REFERENCES properties(pid));

create table tags(pid int, tag varchar(30), primary key(pid,tag), FOREIGN KEY(pid) REFERENCES properties(pid));

create table property_analytics(pid int NOT NULL primary key , distance int);

/* Dummy values */

insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area) values('Beautiful Green House','MurugeshPalya','Buy','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',2,1,1,'12 S R Layout','Bangalore',560017,120300,3020);
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area) values('Beautiful Blue House','MurugeshPalya','Buy','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',1,2,1,'12 S R Layout','Bangalore',560017,120300,3020);
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area) values('House for sale','MurugeshPalya','Buy','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',2,1,1,'12 S R Layout','Bangalore',560017,120300,3020);
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area) values('Villa in domlur','MurugeshPalya','Buy','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',2,1,1,'12 S R Layout','Bangalore',560017,120300,3020);
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area) values('Green Villa','MurugeshPalya','Buy','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',2,1,1,'12 S R Layout','Bangalore',560017,120300,3020);
insert into properties(title, locality, type, short_description, description, bedrooms, bathrooms, patio, address, city, pincode, cost, area) values('Green Bungalow','MurugeshPalya','Buy','A beautiful house in bangalore region with brilliant interior design','This is an amazing house in MurugeshPalya filled with amazing features. The architecture is amazing and 10 top architects have worked on this building. It has taken 5 years to construct this house.',2,1,1,'12 S R Layout','Bangalore',560017,120300,3020);

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

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO root;