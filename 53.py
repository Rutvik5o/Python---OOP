#(53)=> Write a program to demostrate the use of instance and class / static variables.

print("use of class variable")

class sample:

    var=10

    @classmethod

    def new_modify(cls):

        cls.var+=1



s1=sample()
s2=sample()

print("x in s1=> ",s1.var)

print("x in s2=>",s2.var)


s1.new_modify()



print("x in s1=> ",s1.var)

print("x in s2=>",s2.var)


print("Use of Instace Variable")


class sample1:

    def __init__(self):

        self.x=10

    def modify(self):
        
        self.x+=1



s1=sample1()
s2=sample1()

print("x in s1=>",s1.x)

print("x in s2=>",s2.x)


s1.modify()


print("x in s1=>",s1.x)

print("x in s2=>",s2.x)






