#(18)=> Write a program to override the super class method in subclass.

import math

class sqaure:

    def area(self,x):

        print("Area of Square=> ",(x*x))

    
class circle(sqaure):

    def area(self,x):

        print("Area of Circle=> %.2f"%(math.pi*x*x))


c=circle()

c.area(4)