#(11)=> Write a program to override super class constructor and method in sub class.

class teacher:

    def __init__(self):

        self.id=1001

    def display(self):

        print("Teacher Id=> ",self.id)


class student(teacher):

    def __init__(self):

        self.id=1

    def display(self):

        print("Student ID=> ",self.id)


s=student()

s.display()

