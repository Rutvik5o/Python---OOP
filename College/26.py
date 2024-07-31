'''
(16)=> Create a sample list of 7 elements and implement the list methods mentioned:
append,insert,copy,extend,count,remove,pop,sort,reverse & clear.
'''

list1=[1,2,5,53,64,2,25,1]
print(list1)

#append
list1.append(12)
print(list1)

#insert
list1.insert(2,22)
print(list1)

#copy
list2=list1.copy()
print(list2)

#extend
list1.extend(list2)
print(list1)

#count
print(list1.count(2))

#remove
list1.remove(2)
print(list1)

#pop
list1.pop(3)
print(list1)

#sort()
list1.sort()
print(list1)

#reverse
list1.reverse()
print(list1)

#clear()
list1.clear()
print(list1)
