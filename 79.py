#(9)=> Write a program to delte a row from an employee table by accpecting the employee identify number(eid) from the user.

import mysql.connector

try:

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="*****", # enter password
        database="Sample_DB"
    )



    if mydb is None:

        print("Database is not connected")

    else:

        print("Database is connected")

    
    cursor=mydb.cursor()

    id=input("Enter Employee ID which you want to delete record=>")

    sql="delete from employee where empid=%s"

    val=(id,)

    cursor.execute(sql,val)

    print("Record Deleted")

    mydb.commit()

    #Advance Functionlity

    while("True"):

        choice=input("would you like to show remaining data?->")

        if(choice == "Yes" or choice =="yes"):

            cursor.execute("select * from employee")

            remaining_data=cursor.fetchall()

            print("Remaining Data=>")

            for row in remaining_data:
                empid, empname, sal = row
                print(f"({empid}, {empname}, {float(sal)})")

            '''
            for row in remaining_data:
                print(row)
            '''

        
        elif(choice == "No" or choice == "no"):

            print("Exited")

            break

        else:

            print("Wrong input!!")


        

except mysql.connector.Error as e:

    print("Error=> ",e)
