#(16)=> Create a sample list of 7 elements and implement the list methhods mentioned: append, insert, copy, extend,count, remove, pop, sort , reverse and order.

list1=[i for i in range(1,6)]

print(list1)

#append

list1.append(50)

print(list1)

#insert

list1.insert(2,12)

print(list1)

#copy

list2=list1.copy()

print(list2)

#extend

another_list=[35,63,6,50]

list1.extend(another_list)

print(list1)

#count

print(list1.count(50))

#remove

list1.remove(50)

print(list1)

#pop

print(list1.pop())

#sort

list2=[5,43,85,369,47,15]

list2.sort()

print(list2)

#reverse

list1.reverse()

print(list1)

#clear

list2.clear()

print(list2)



