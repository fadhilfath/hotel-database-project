drop table if exists Room_Book;
drop table if exists Room_Type;
drop table if exists Building;
drop table if exists Address;
drop table if exists Visitor;

create table Visitor
	(visitor_id		int(10), 
	 first_name		varchar(45), 
	 last_name		varchar(45),
	 arrival_date	DATE,
	 leaving_date	DATE,
	 phone_number	int(11),
	 deposit		float(5),
	 primary key 	(visitor_id)
	);


create table Address
	(visitor_id 	int(10),
	 street			varchar(15),
	 city			varchar(15),
	 code			varchar(45),
	 primary key (visitor_id),
	 foreign key(visitor_id) references Visitor(visitor_id)
	);
	
create table Building
	(building_id	int(11), 
	 building_name	varchar(11), 
	 primary key (building_id)
	);

create table Room_Type
	(room_number    int(11),
	 building_id	int(11),
	 room_available boolean,
	 room_type      varchar(45),
	 price			float(4),
	 primary key(room_number,building_id),
	 foreign key(building_id) references Building(building_id)
	);
	
create table Room_Book
	(room_number	int(11), 
	 visitor_id		int(10), 
	 room_upgrade	BOOL,
	 primary key (room_number,visitor_id),
	 foreign key(room_number) references Room_Type(room_number),
	 foreign key(visitor_id) references Visitor(visitor_id)
	);
		
