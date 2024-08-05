'''
(10)=> write a program to show variable length argument & its use
'''

def my_function(*args):

    print("The youngest Child=>", args[2])



my_function("first","second","third","fourth")