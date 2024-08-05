'''
(17)=> Write a program to create nested list and display its elements.
'''


nested_list = [10,20,30,['a','b','c']]

sub_list = nested_list[3]

data = nested_list[3][1]

print("List inside the nested list =>",sub_list)

print("Second Elements of the sub list>",data)