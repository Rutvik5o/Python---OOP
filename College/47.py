'''
(7)=>Create a Bank class with two variables name and
balance. Implement a constructor to initialize the
variables. Also implement deposit and withdrawals
using instance methods.
'''


class Bank:

    def __init__(self,name,balance):

        self.ename = name

        self.ebalance = balance


    def display(self,deposit,withdrawls):

        print("Name =>",self.ename)

        print("Balance =>",self.ebalance)

        print("Deposit=>",deposit)

        print("Witdrawls=>",withdrawls)


obj1=Bank("ABC",50000)
obj1.display(1000,2000)
Bank.display(obj1,200,300)