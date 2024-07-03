#(10)=> Wirte a program to show variable length arugment and its use.

def variable_length(*args):

    for value in range(0,len(args)):

        print(args[value])


variable_length("A","B","C","D","E")