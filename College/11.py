'''
(1)=> Write a program to create one array from another array.
'''

arr1=[0,76,454,32,12,34]

arr2= [None] *  len(arr1)

for i in range(0,len(arr1)):
    arr2[i]=arr1[i]


print("Printing Original array->")

for i in range (0,len(arr1)):
    print(arr1[i])

print("Printing new array->")

for i in range (0,len(arr2)):
    print(arr2[i])

