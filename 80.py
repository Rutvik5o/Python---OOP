#(10)=> Write a program to increase the salary(sal) of an employee in the employee table by accpecting the employee identify number (eid) from the user.


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

    empid=input("Enter Employee ID=>")

    increment=int(input("Enter Increment Amount->"))

    sql="update employee set sal=sal + %s where empid = %s"

    val=(increment,empid,)

    cursor.execute(sql,val)

    print("Record Updated")

    mydb.commit()


    #additional functionlity

    while("True"):

        choice=input("would you like to show updated data?->")

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

    print("Error=>",e)

        
