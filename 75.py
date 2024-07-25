#(5)=> Write a program to import datetime and format the data as required. Also use the same moudle to calculate the difference between your birthday and today in days.

import datetime

year=int(input("Enter your birth year->"))

month=int(input("Enter your birth month->"))

date=int(input("Enter your birth date->"))

birthday=datetime.datetime(year,month,date)

now=datetime.datetime.now()

difference=now-birthday

print("Difference is => ",difference.days,"days")