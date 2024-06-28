#(8)=> Write a python program to find the sum of even numbers using command line arguments.



import sys


def is_even(number):
    return number % 2 == 0


def sum_even(numbers):
    even_num= [num for num in numbers if is_even(num)]
    return sum(even_num)



if __name__ == "__main__":

    #exclude the script name from the argument

    args=sys.argv[1:]

    #converts arguments to integers


    try:
        numbers = [int(arg) for arg in args]

    except ValueError:
        print("Please provide only integer arguments.")
        sys.exit(1)


    result = sum_even(numbers)
    print("The sum of even numbers=>",result)

