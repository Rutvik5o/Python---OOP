#Insert Data manually


import mysql.connector


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

    cursor.execute("insert into employee values('EMP01','XYZ','15000')")
    cursor.execute("insert into employee values('EMP02','ABC','85000')")
    cursor.execute("insert into employee values('EMP03','MNO','17000')")
    cursor.execute("insert into employee values('EMP04','QWT','93000')")
    cursor.execute("insert into employee values('EMP05','IOU','71000')")


    print("New table created")

    mydb.commit()


except mysql.connector.Error as e:

    print(e)




        