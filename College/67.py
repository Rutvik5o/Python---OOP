'''
(7)=> Write a program to retrieve and display all the rows in the 
employee tabl (first create an employee table in the sample_db with the
fields as eid,name,sal also enter some valid records.)
'''

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "***" #Enter Your password
    database = "Sample_DB"
)

try:

    if mydb is None:

        print("Database is not connected")
    
    else:

        print("Database connected successfully")

except mysql.connector.Error as e:
    print(e)


else:
    print("You can start your work")


a= mydb.cursor()

b= a.execute("select * from employee")

result = a.fetchall()

for x in result:
    print(x)

mydb.commit()
mydb.close()


