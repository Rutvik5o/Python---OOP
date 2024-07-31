'''
(3)=> Write a program to understand various methods of array class
mentioned: append,insert,remove,pop,index,tolist & count
'''

from array import *

a=array('i',[1,3,45,34,65,34,24,53])

print("Printing full array")

for i in range(8):
    print(a[i])


a.append(10)
print(a)

a.insert(2,101)
print(a)

a.pop(2)
print(a)

a.remove(24)
print(a)

print(a.index(34))

print(a.count(34))

print(a.tolist())


'''
Type Codes:
The array module uses type codes to specify the type of elements in the array. Here are some common type codes:

'b': signed char (1 byte)
'B': unsigned char (1 byte)
'h': signed short (2 bytes)
'H': unsigned short (2 bytes)
'i': signed integer (4 bytes)
'I': unsigned integer (4 bytes)
'l': signed long (4 bytes)
'L': unsigned long (4 bytes)
'f': float (4 bytes)
'd': double (8 bytes)
'''
