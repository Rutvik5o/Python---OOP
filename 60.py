#(10)=> Write a program to access the base class constructor from a sub class by using super() method and also without using super() method.


class square:

    def __init__(self,x):

        self.x=x

    def area(self):

        print("Area of Square=> ",self.x * self.x)



class rectangle(square):

    def __init__(self,x,y):

        super().__init__(x)

        self.y=y

    def area(self):

        super().area()

        print("Area of Rectangle=> ",self.x * self.y)


a,b= [float(x) for x in input("Enter Length and breadth=>").split()]

r=rectangle(a,b)

r.area()


