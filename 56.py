#(6)=> Write a program to create astatitc method that counts the number of instancs created for a class.


class myclass:

    n=0

    def __init__(self):

        myclass.n+=1



    @staticmethod

    def no_of_objects():

        print("no of instances crated are", myclass.n)


obj1=myclass()

obj2=myclass()

obj3=myclass()


myclass.no_of_objects()