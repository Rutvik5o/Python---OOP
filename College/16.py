'''
(6)=> Write a program to generate prime numbers with the 
help of a functio to test prime or not.
'''


def checkprime():
    num = int(input("Enter a number -> "))

    if num <= 1:
        print(num, "is not a prime number")
        return
    
    c = 0
    
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1

    if c == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

checkprime()
