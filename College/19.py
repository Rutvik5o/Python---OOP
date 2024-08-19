'''
(9)=> Write a program to demostrate the use of positional argument,
keyword argument & default argument
'''


def my_function(fname,lname):

    print(fname + " "+lname)

my_function("abc","xyz")
#Positional arguments are passed in the order defined in the function.


def my_function(child3,child2,child1):

    print("The youngest children->",child3)
#Keyword arguments specify the parameter name and can be passed in any order.

my_function(child1 = "one",child2= "second",child3="three")


def my_function(country="Norway"):
    
    print("i am from",country)

#Default arguments are used if no value is provided for the parameter.


my_function("India")
my_function()
my_function("Brazil")
my_function("Canada")

