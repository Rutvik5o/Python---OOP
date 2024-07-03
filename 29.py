#(9)=> Write a program to demostrate the use of Posistional arguments keyword argument and default argument.

#Positional Argument

def positional(ram,shyam,harish):

    print(ram,shyam,harish)


a="Ram"
b="Shyam"
c="Harish"


positional(a,b,c)

#Keyword argument


def keyword(ram,shyam,harish):

    print(ram,shyam,harish)
    


a="Ram"
b="Shyam"
c="Harish"

keyword(ram=a,harish=c,shyam=b)
# keyword(ram=a,shyam=c,harish=b)


#Default Argument

def Keyword(ram,shyam,harish="Harish"):

    print(ram,shyam,harish)

a="Ram"
b="Shyam"

Keyword(ram=a,shyam=b)

