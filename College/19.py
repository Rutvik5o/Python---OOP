'''
(9)=> Write a program to demostrate the use of positional argument,
keyword argument & default argument
'''


def my_function(fname,lname):

    print(fname + " "+lname)

my_function("abc","xyz")


def my_function(child3,child2,child1):

    print("The youngest children->",child3)


my_function(child1 = "one",child2= "second",child3="three")


def my_function(country="Norway"):
    
    print("i am from",country)

my_function("India")
my_function()
my_function("Brazil")
my_function("Canada")

