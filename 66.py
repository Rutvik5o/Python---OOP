#(16)=> Write a program to overload the addition operator(+) to make act on the class object.


class bookx:

    def __init__(self,pages):

        self.pages=pages

    def __add__(self,other):

        return self.pages - other.pages # +
    
class booky:

    def __init__(self,pages):

        self.pages=pages


b1=bookx(100)
b2=booky(150)


print("Total Pages=> ",(b1+b2))