'''
(9)=> Write a program in search an element in the list using for loop 
and also demostrate the use of "else" with for loop.

''' 

list1=[3,5,363,36,2,74]

n=0

a=int(input("Enter number you want to search->"))

for x in list1:

    if(x==a):
        print("Given Element Exist->",x)
    else:
        n=+1

if(n==len(list1)):
    print("Given elementt does not exist->",a)





'''
list1 = [3, 5, 363, 36, 2, 74]

a = int(input("Enter number you want to search: "))

for x in list1:
    if x == a:
        print("Given element exists:", x)
        break
else:
    # This block will execute if the loop completes normally (i.e., no break)
    print("Given element does not exist:", a)

'''
