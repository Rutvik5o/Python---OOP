'''
(4)=> Write a program to store data into instances using mutator method and to retrieve 
data from the instances using accessor methods.
'''


class student:

    def __init__(self):

        self.name = "ABC"


    def get_name(self):

        return self.name
    
    def set_name(self):

        self.name = "XYZ"


s1=student()
print("Before setter method name is->",s1.get_name())

s1.set_name()

print("After setter method name is->",s1.get_name())