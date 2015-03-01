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
       nmea_sentence	varchar(255)	null,
       noun		varchar(15)	not null,
       description	varchar(255)	not null,
       spd_over_grnd_kts	float	null,
       wind_speed		float 	null,
       hdg_true			varchar(15)	null,
       vel_units		varchar(15)	null,
       correction_dir		varchar(15)	null,
       local_zone		float 	null,	
       depth_feet		float 	null,
       data_valid		varchar(15) null,
       msg_num			float	    null,
       magnetic			varchar(15) null,
       mag_track		varchar(15) null,
       status			varchar(15) null,
       heading			float	    null,
       velocity			float	    null,
       cross_track_err_dist	float	    null,
       timestamp		varchar(15) null,
       depth_fathoms		float	    null,
       elevation_deg_1		float	    null,
       elevation_deg_2		float	    null,
       elevation_deg_3		float	    null,
       elevation_deg_4		float	    null,
       true_track_sym		varchar(15) null,
       wind_speed_units		varchar(15) null,
       waypoint_id		varchar(15) null,
       warning_flag		varchar(15) null,
       month			float	    null,
       year			float	    null,
       day			float	    null,
       feet			varchar(15)    null,
       lat			varchar(15) null,
       lon			varchar(15) null,
       lon_dir			varchar(15) null,
       lat_dir			varchar(15) null,
       num_messages   		varchar(15) null,
       knots			varchar(15)    null,
       spd_over_grnd_kmph_sym	varchar(15) null,
       wind_angle		float		null,
       dist_units		varchar(15) null,
       meters			varchar(15) null,
       faa_mode			varchar(15) null,
       spd_over_grnd_kmph	float		null,
       reference		varchar(15) null,
       lock_flag		varchar(15) null,
       local_zone_minutes	float null,
       fathoms			varchar(15) null,
       snr_1			varchar(15) null,
       snr_2			varchar(15) null,
       snr_3			varchar(15) null,
       snr_4			varchar(15) null,
       direction_true		float null,
       water_speed_km		float null,
       true_track		float null,
       depth_meters		float null,
       azimuth_1		float null,
       azimuth_2		float null,
       azimuth_3		float null,
       azimuth_4		float null,
       direction_magnetic	float null,
       wind_speed_knots		float null,
       heading_true		float null,
       heading_magnetic		float null,
       spd_over_grnd_kts_sym      varchar(15) null,
       wind_speed_meters	  float null,
       water_speed_knots	  float null,
       kilometers		  varchar(15) null,
       mag_track_sym		  varchar(15) null,
       sv_prn_num_1		  varchar(15) null,
       sv_prn_num_2		  varchar(15) null,
       sv_prn_num_3		  varchar(15) null,
       sv_prn_num_4		  varchar(15) null,
       num_sv_in_view		  float null
);
