#(17)=>Write a program to create nested list and display its elements.

list1=[[1,2,3],[4,5,6],[7,8,9,10]]

for x in list1:
    print(" ".join(map(str,x)))