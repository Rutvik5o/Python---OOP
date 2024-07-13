#(14)=> Write a program to understand the order of execution of methods in several base classes according to method resoultion order (MRO).

class A(object):
    
    def method(self):

        print(" A class method")

        super.method()



class B(object):
    
    def method(self):

        print("B class method")

        super.method()

class C(object):
    
    def method(self):

        print("C class method")

        super.method()

class X(A,B):

    def method(self):

        print("X Class method")

        super.method()

class Y(B,C):

    def method(self):

        print("Y Class Method")


class P(X,Y,C):

    def method(self):

        print("P class method")

        super().method()



newp=P()

print(P.mro())

newp.method()


'''
class Base(object):
    def method(self):
        pass  # Default implementation that does nothing

class A(Base):
    def method(self):
        print("A class method")
        super().method()

class B(Base):
    def method(self):
        print("B class method")
        super().method()

class C(Base):
    def method(self):
        print("C class method")
        super().method()

class X(A, B):
    def method(self):
        print("X class method")
        super().method()

class Y(B, C):
    def method(self):
        print("Y class method")
        super().method()

class P(X, Y, C):
    def method(self):
        print("P class method")
        super().method()


newp = P()


print(P.mro())

newp.method()
'''


