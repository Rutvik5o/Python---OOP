'''
(5)=> Write a program to import datetime module and format the data as required also use the same to calculate the difference between your birthday and todays in day.
'''


import datetime


today=datetime.date.today()

birthday = datetime.date(1987,4,3)

diff = today - birthday

print(diff.days,"Days ")