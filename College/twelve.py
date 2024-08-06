'''
(12)=> Write a python program that asks the user to enter a length in centimeter. if the user enters a negative length,
the program should tell the user that entry is invalid. Otherwise, the program should convert the length to inches 
and print out the result(2.54 = 1 inch).
'''
len=int(input("Enter Length in Centimeter->"))

if len < 0:

    print("Invalid Input")

else:

    inch = len / 2.54

    print(len, "Centimeter is equal to =>",inch,"inches")

