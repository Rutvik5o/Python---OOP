'''
(11)=> Write a program to override super class constructor 
and method in sub class.
'''

class parent():

    def __init__(self):

        self.value = "Parent"


    def show(self):

        print(self.value)


class child(parent):

    def __init__(self):

        super().__init__()

        self.value = "Child"


    def show(self):

        print(self.value)

        

obj1=child()
obj1.show()