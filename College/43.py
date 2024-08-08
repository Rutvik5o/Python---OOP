'''
(3)=> Write a program to demostrate the use of instance & class/static variable

'''


class student:

    dept = "IT"

    def __init__(self,r,n):

        self.roll = r
        
        self.name = n


obj1=student(10,"ABC")

print(obj1.roll)

print(obj1.name)

print(obj1.dept)

print(student.dept)
