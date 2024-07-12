#(12)=> Write a program to implement single inheritence in which two sub classes are derived from a single base class.

class Bank(object): 

    cash=100000

    @classmethod

    def chk_cash(cls):
        
        print(cls.cash)


class Andhrabank(Bank):
    pass



class Statebank(Bank):

    cash=20000

    @classmethod
    
    def chk_cash(cls):

        print(cls.cash+Bank.cash)


a=Andhrabank()

a.chk_cash()

s=Statebank()

s.chk_cash()


