# hotel-database-project

##CREATING A HOTEL DATABASE USING MYSQL

###Course: CSCI 3287- Fall 2015
###Team members: Fadhil Fathurrahman Suhendi, Phu Dang, Thao Le
###Project was revised by professor Richard Osborne in 12/9/2015.

####This project package includes:
-hotel_database.sql      : file uses to create hotel database
-hoteldb_uml_diagram.mwb : contains the E-R Diagram for hotel database (this file should be opened in mysqlworkbench)
-hotel_schema.sql        : contains the schema of hotel database
-sample_queries.txt      : contains the list of sample queries
-project2.py             : contains the code to create the interfaces to let the user interact to our database

####Instruction to create and run the database:
- create user ‘username’@’localhost’ identified  by ‘password’
- create a new database called hotel
- import a db schema into mysql with the following command:
mysql –u ‘username’ –p ‘database_name’ < filename.sql (database file is provided in the folder)

####Instruction to run the project:
-Run hotel_database.sql in mySQL to create the hotel database.
-Run project.py to launch the interface (Install all required libraries).

