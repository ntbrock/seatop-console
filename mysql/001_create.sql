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
       created_on	timestamp   not null,
       created_by	varchar(63)   not null default 'Brockman/Illyria/Charleston/SC/USA',
       last_gps_on	datetime	null,
       last_gps		point	null,
       last_lat		decimal(10,8)	null, -- Stored in decimal format for everyone else 
       last_lon		decimal(11,8)	null,
       sentence		varchar(255)	null,
       noun		varchar(15)	not null,
       p0s		varchar(15)	null,
       p0f		float	null,
       p1s		varchar(15)	null,
       p1f		float	null,
       p2s		varchar(8)	null,
       p2f		float	null,
       p3s		varchar(8)	null,
       p3f		float	null,
       p4s		varchar(8)	null,
       p4f		float	null,
       p5s		varchar(8)	null,
       p5f		float	null,
       p6s		varchar(8)	null,
       p6f		float	null,
       p7s		varchar(8)	null,
       p7f		float	null,
       p8s		varchar(8)	null,
       p8f		float	null,
       p9s		varchar(8)	null,
       p9f		float	null,
       p10s		varchar(15)	null,
       p10f		float	null,
       p11s		varchar(15)	null,
       p11f		float	null,
       p12s		varchar(8)	null,
       p12f		float	null,
       p13s		varchar(8)	null,
       p13f		float	null,
       p14s		varchar(8)	null,
       p14f		float	null,
       p15s		varchar(8)	null,
       p15f		float	null,
       p16s		varchar(8)	null,
       p16f		float	null,
       p17s		varchar(8)	null,
       p17f		float	null,
       p18s		varchar(8)	null,
       p18f		float	null,
       p19s		varchar(8)	null,
       p19f		float	null
);

