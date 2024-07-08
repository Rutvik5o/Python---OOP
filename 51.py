#(1)=> Write a program to create a student class with name,age and marks as data memebers. Also create a method name display() to view the student
# details. Create an object to student class and call the method using the object.

class student:

    def __init__(self):

        self.name="xyz"

        self.age=23

        self.marks=79


    def display(self):

        print("Name=> "+self.name)

        print("Age=>",self.age)

        print("Marks=>",self.marks)


a=student()
a.display()