'''
(53)=> Write a program to implement multiple inheritence using two base classes.
'''

class A():

    def fun1(self):

        print("From class a")

class B():

    def fun2(self):

        print("From class b")


class C(A,B):

    def fun3(self):

        print("From class c")


obj1=C()
obj1.fun1(),obj1.fun2(),obj1.fun3()