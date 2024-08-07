'''
(1)=> Write a program to create a student class with name,age and marks as data member. Also create a mehod named display() to view the student details. 
create an object to student class and call the method using the object.
'''


class Student:

    def __init__(self,name,age,marks):

        self.name = name
        self.age = age
        self.marks = marks


    def display(self):

        print(self.name , self.age , self.marks)


s1=Student("abc",19,89)
s1.display()




