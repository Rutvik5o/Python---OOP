#(2)=> Create a program to retrieve, display and update only a range of elements from an array using indexing and slicing in arrays.


import array as arr

a=arr.array('i',[1,2,3,4,5])

print(a)

a[0]=7

print(a)
#update array using slicing

a[0:2]=arr.array('i',[8,9])

print(a)