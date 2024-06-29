#(11)=>Write a program to search an element in the list using for loop and also demostrate the use of "else" with for loop.

def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            return True
    else:
            return False
        


list = [1,2,'Sachin',4,'Python',6]

n=input("Enter item you want to search=>")


if search(list,n):
    print("Item Found")
else:
    print("Item not found")

#New Approach

# def search(lst, n):
#     for item in lst:
#         if item == n:
#             return True
#     else:
#         # This block executes if the loop completes without finding the item
#         return False

# lst = [1, 2, 'Sachin', 4, 'Python', 6]

# n = input("Enter item you want to search: ")

# if search(lst, n):
#     print("Item Found")
# else:
#     print("Item not found")
