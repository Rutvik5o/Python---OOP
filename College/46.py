'''
(6)=> Write a program to create a static method that counts the number of 
instances created for a class.
'''

class Student:

    counter = 0

    def __init__(self):

        Student.counter += 1

    @staticmethod

    def display():

        print("Total Object Created=>",Student.counter)


Obj1=Student()
Obj2=Student()
Obj3=Student()
Obj3.display()

    




