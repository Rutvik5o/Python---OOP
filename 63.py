#(13)=> Write a program to implement multiple inheritance using two base classes.

class Father:
    
    def height(self):

        print("Heigh is 6.0 foot")


class Mother:

    def complexion(self):

        print("Complexion is Fair")


class Child(Father,Mother):

    pass


print("Child Inherited Qualities:")
c=Child()

c.height()

c.complexion()

