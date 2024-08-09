#(7)=> Write a program to retrieve and display all the rows in the employee table. [First create an employee table in the Sample_DB  with the fields as eid,name,sal. Also enter some valid records.] 

#Creation of table   


import mysql.connector

try:

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="rutvik#545250",
        database="Sample_DB"
    )

    if mydb is None:

        print("Database not connected")

    else:

        print("Database is connected")


    cursor=mydb.cursor()

    cursor.execute("create table employee(empid varchar(10) primary key,empname varchar(50),sal numeric(15))")

    print("Employee table created successfully")

except mysql.connector.Error as e:
    
    print(e)