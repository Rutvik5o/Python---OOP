#(15)=> Write a program to combine two list, perform repetition of lists and create cloning of lists.

list1=[i for i in range(1,6)]

list2=[i for i in range(7,11)]

print(list1)

print(list2)

list3=list1+list2

#Repetition of list

new_list=[i for i in list3 for x in(0,1)]

print(new_list)

#cloning of list

list_cloning=list3[:]

print(list_cloning)