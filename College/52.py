'''
(52)=> Write a program to implement single inheritence in which two sub classes
are derived from a single base class.
'''

class A():

    p1="from class a"

class B(A):

    p2 = "from class b"

class C(A):

    p3 = "from class c"


obj1 = B()
print(obj1.p1)

obj2=C()
print(obj2.p1,obj2.p3)