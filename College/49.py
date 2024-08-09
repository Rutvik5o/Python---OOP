'''
(8)=> Write a program to create a Emp class & make all the members of the
Emp class available to another class (Myclass). [By passing members of one class to another]
'''

class parent:

    x=5

    def fun1(self):

        print("Parent Class")


class child(parent):

    y=10

    def fun2(self):

        print("Sub Class")


obj1=child()
print(obj1.x)
print(obj1.y)
obj1.fun1()
obj1.fun2()