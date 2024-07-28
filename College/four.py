'''
(4)=> Write a program to find add display the common and non common 
elements in the list using membership operators.
'''


list1=[1,2,3,5,3,2,56,6]
list2=[2,4,5,6,8,3]


c=[]
nc=[]

for x in list1:
    if (x in list2):
        c.append(x)
    else:
        nc.append(x)


print("Common Elements-> ",c)

print("Non Common Elemnts-> ",nc)