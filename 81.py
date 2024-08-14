#(11)=> Write a program to create a table named new_employee_tbl with the fields eno,ename,gender and salary in Sample_DB database. The datatype of the fileds are eno-int, enamechar(30), gender-char(1) and salary-float.


import mysql.connector

try:

    mydb=mysql.connector.connect(

        host="localhost",
        user="root",
        password="***", #enter password
        database="Sample_DB"
    )


    if mydb is None:

        print("Database not connected")

    else:

        print("Database is connected")



    cursor=mydb.cursor()

    cursor.execute("create table new_employee_tbl(eno int primary key,ename varchar(30),gender char(1),salary float)")

    print("New Table Created")

    mydb.commit()

except mysql.connector.Error as e:

    print("Error=> ",e)
