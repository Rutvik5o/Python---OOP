#(5)=> Write a program to find out and display the common and the non common elements in the list using membership operators.

a=10
b=20

list=[1,2,3,4,5]

if (a in list):
    print("Line 1: a is available in the given list")

else:
    print("Line 1: a is not available in the given list")



if(b in list):
    print("Line 2: b is available to the given list")

else:
    print("Line 2: b is not available to the given list")


a=2

if(a in list):
    print("Line 3: a is available to the given list")

else:
    print("Line 3: a is not available in the given list")