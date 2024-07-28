'''
(5)=> Write a program to display memoery locatios of two variable using id() function and the use identify operator two compare whether two comparee whether two object are same or not.
'''


a=10
b=10

print("Memory Location of a->",id(a))
print("Memory Location of b->",id(b))


if (a is b):
    print("a and b have same identify")
else:
    print("a and b not have same indentify")
