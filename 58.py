#(8)=> Write a program to create a emp class and make all the members of the emp class available to another class (MyClass). [By passing members of one cass to another]


class Emp:

    def __init__(self,id,name,sal):

        self.id=id
        self.name=name
        self.salary=sal


    def display(self):

        print("ID=> ",self.id)

        print("Name=> ",self.name)

        print("Salary=> ",self.salary)

    

class MyClass:

    @staticmethod

    def mymethod(e):

        e.salary += 1000
        e.display()

    

e=Emp(1001,"XYZ",12000)

MyClass.mymethod(e)







