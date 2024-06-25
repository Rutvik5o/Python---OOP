#(1)=> write a program to swap two numbers without taking a temporary variable


a=int(input("Enter value of first variable->"))

b=int(input("Enter value of second variable->"))

a=a+b #a=10 b=20 a=30
b=a-b #a=30 b=20 b=10
a=a-b #a=30 b=10 a=20


print("A=> ",a,"\nB=> ",b)