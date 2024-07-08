#(2)=> Write a program to create student class with a constructor having more than one parameter.

class student:

    def __init__(self,nm="none",ag=15,m=0):

        self.name=nm
        self.age=ag
        self.marks=m

    def display(self):

        print("Name=> ",self.name)

        print("Age=> ",self.age)

        print("Marks=> ",self.marks)


x=student()
x.display()

b=student("xyz",20,50)
b.display()