'''
(10)=> Write a program to access the base class constructor from a sub class
by using super() method and also without using super() method.
'''

class parent():

    def __init__(self):

        print("to program")


class child(parent):

    def __init__(self):

        print("welcome")

        super().__init__()

        #parent.__init__(self)

b1=child()