#(6)=> Write a program to create a database named "Sample_DB" in MySQL().
#[First ensure connection is made or not and then check if the database Sample_DB already exists or not, ifyes then print appropriate message].


import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password="*********"  #enter password
)


print(mydb)



try:

    cursor=mydb.cursor()
    cursor.execute("Create Database Sample_DB2")
    cursor.execute("Show Databases")
    my=cursor.fetchall()
    print("Database Created")

    for i in my:
        print(i)

except mysql.connector.Error as e:

    print(e)