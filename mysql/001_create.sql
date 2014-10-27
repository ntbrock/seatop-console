-- Welcome to the Seatop mysql schema!
-- Raspberry pi can run mysql and I figured a SQL interface is best way 
-- to query / explore NMEA captured GPS data.

drop table evolutions;
create table evolutions (
       id    integer	primary key auto_increment,
       filename	varchar(255)	not null unique,
       created_on	datetime    not null
);


drop table nmeas;
create table nmeas (
       id    integer	primary key auto_increment,
       last_gps		point	null,
       last_

       filename	varchar(255)	not null unique,
       created_on	datetime    not null
);

