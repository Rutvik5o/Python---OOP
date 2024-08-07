'''
(2)=> Write a program to create student class with  
constructor having more than one parameter.
'''


class Student:

    def __init__(self,n,a,m):

        self.name = n
        self.age = a
        self.marks = m

    def display(self):
        print("Student Name =>",self.name)
        print("Student Age => ",self.age)
        print("Student Marks=>",self.marks)



s1=Student("Xyz",20,98)
s1.display()