'''
(5)=> Write a program to use class method to handle the common feature of all 
the instances created for a class.
'''


class student:

    dept = "BCA"  #class variable


    def __init__(self,r,n):

        self.roll = r

        self.name = n


    def display(self):

        print("Roll Number=>",self.roll)

        print("Department=>",self.dept)


obj1=student(1,'abc')
obj1.display()

obj2=student(2,'xyz')
obj2.display()