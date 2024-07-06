#(19)=> Create a program to sort tuple with nested tuples.

typ=[(1,(2,3)),(3,(2,1)),(2,(2,1))]

sort_tup=sorted(typ,key=lambda t: (t[1][1],t[0]))

print(sort_tup)