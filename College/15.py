'''
(5)=> Create a program to search the position of an element in 
an array using index() method of array class.
'''


from array import *

a=array('i',[1,2,35,23,36,2])

print("Full Array printing->")


for i in range(6):
    print(a[i])

print("Position of elemnts is=>",a.index(23))
