#(17)=> Write a program to show method overloading to find sum of two or three memebers.

class myclass:

    def sum(self,a=None,b=None,c=None):

        if a!= None and b!= None and c!=None:

            print("Sum of three Number=> ",(a+b+c))

        elif a!=None and b!= None:

            print("Sum of two number=> ",(a+b))

        else:

            print("Pass atleast 2 or 3 argument")


x=myclass()

x.sum(10,20,30)

x.sum(10,20)

x.sum(10)

x.sum()