#(6)=> Write a program to generate prime numbers with the help of a function to test prime or not.


def test_prime(num):

    if num>1:

        for i in range(2,num):

           if  (num % i) == 0:
               
               print(num," is not a prime number")

               break

        else:

            print(num, "is a prime number")

    else:

        print(num," is a prime number")

num=int(input("Enter Number to check prime or not=>"))

test_prime(num)

