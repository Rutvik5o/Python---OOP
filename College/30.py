'''
(20)=> Write a program to create a dictionary from the user and display the element
'''

user_dict = {}


num_entries = int(input("Enter the number of entires you want->"))

for i in range(num_entries):

    key=input("Enter Key->")

    value=input("Enter Value->")

    user_dict[key]=value

print("Dictionary After adding user input=>",user_dict)