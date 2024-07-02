#(7)=>Write a python program that removes any repeated items from a list so that each item appears at most once. For instances, the list [1,12,3,4,3,0,0] would become [1,2,3,4,0]


li=[1,2,3,3,4,3,5,5,5,6,6,7,7,12,12]

li2=[]

for i in li:

    if i not in li2:

        li2.append(i)


print(li2)