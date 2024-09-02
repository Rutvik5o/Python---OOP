'''
(1)=> Write a program to handlesome built in exceptions like zero division error.
'''


a=int(input("Enter First Number->"))

b=int(input("Enter Second Number->"))

try:
    c=a/b
    print(c)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

else:
    print("Thanks!! Program completed successfully")

