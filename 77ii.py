# Retrieve data

import mysql.connector
from mysql.connector import errorcode
from decimal import Decimal

try:

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="rutvik#545250",
        database = "Sample_DB"
    )

    if mydb is None:

        print("Databse not connected")

    else:

        print("Database is connected")



    cursor= mydb.cursor()

    cursor.execute("select * from employee")

    rows=cursor.fetchall()

    #print(rows)

    #to display all records

    for row in rows:
        row = tuple(str(item) if isinstance(item, Decimal) else item for item in row)
        print(row)
        
    '''

    for i in rowws:
        print(i)
    '''

    mydb.commit()



except mysql.connector.Error as e:
    
    print(e)
