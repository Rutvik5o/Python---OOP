#(8)=> Write a program to insert several rows into employee table from the keyboard.

import mysql.connector

try:

    mydb=mysql.connector.connect(

        host="localhost",
        user="root",
        password="123",
        database="Sample_DB"
    )


    if mydb is None:

        print("Database is not connected")

    else:

        print("Database is connected")

    
    cursor=mydb.cursor()


    while('True'):

        choice=input("Would you like to enter record-> ")

        if(choice == "Yes" or choice == "yes"):

            empid=(input("Enter Employee ID->"))

            empname=input("Enter Employee name->")

            salary=int(input("Enter Employee Salary->"))


            sql="insert into employee (empid,empname,sal) values (%s,%s,%s)"  #placeholders %s represent the positions where the actual values will be inserted. =>used in python for parameterized query


            val=(empid,empname,salary)

            cursor.execute(sql,val)

            mydb.commit()

            print("Data successfully inserted.")


        elif (choice == "No" or choice=="no"):
            
            break

        else:
            print("Wrong Input")


except mysql.connector.Error as e:

    print("There is Error->",e)


              


        
        
