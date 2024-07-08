#(43)=> Create a python function to accpect python function as a dictionary and display its elements.

def func(d):

    for key in d:

        print("Key:",key,"Value:",d[key])



D={'a':1,'b':2,'c':3}

func(D)