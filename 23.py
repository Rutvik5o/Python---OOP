#(3)=>Write a program to understand various methods of array class mentioned: append, insert, remove , pop, index, tolist and count.

import numpy as np

list1=[1,2,3,4,5,6,7]

list1.append(10)

list1.insert(2,20)

print(list1)



list1.remove(2)

print(list1)

list1.pop()

print(list1)

print(list1.index(3))

print(list1.count(4))



arr=np.array([9,544,3,22,31])

print(arr.tolist())




