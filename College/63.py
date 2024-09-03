'''
(3)=> Write a program to import os moudle and to print the current working 
directory and return a list of all module function.
'''


import os

current = os.getcwd()

print("Current Directory=>", current)

print(dir(os))
