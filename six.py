#(6)=> Create a progam to display memoery locations of two variables using id() function. and the use indentify operators two compares whether two objects are same are not.

a=20

b=20

if(a is b):
    print("Line 1: a and b have same identify")
else:
    print("Line 1: a and b do not have same indentify")



if(id(a)==id(b)):
    print("Line 2: a and b have same identify")
else:
    print("Line 2: a and b not have same identify")



b=30
print("B's value changed")


if(a is b):
    print("Line 3: a and b have same identify")
else:
    print("Line 3: a and b not have same indentify")



if(id(a)==id(b)):
    print("Line 4: a and b have same identify")
else:
    print("Line 4: a and b not have same identify")



