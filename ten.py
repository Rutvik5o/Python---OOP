#(10)=> Write a program to assert the user enters a number greater than zero.

num=int(input("Enter a Number->"))

assert num>=0,"Only Enter Positive Number."

print("You Entered=>",num)