'''
(14)=> Write a program to create a list using range functions and perfrom 
append,update & delete elements operations in it.
'''

list1 = list(range(0,10))
print(list1)

#Append
list1.append(10)
print(list1)

#Update
list1[2]=14
print(list1)

#Delete
list1.pop(5)
print(list1)