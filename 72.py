#(2)=> Write a progam to handle multiple exception like SyntaxError & TryError.


try:

    a=eval(input("Enter a dividend->"))

    b=eval(input("Enter a divisor->"))

    Ans=a/b

except (TypeError,SyntaxError):

    print("Ther is TypeError or Syntax error")


else:

    print("Answer=>",Ans)




# Key difference between int & eval function


'''
(1) Safety: int() is safer than eval() since it only converts to the string to an integer,whereas eeval(0 can excture arbitary code.

(2) Explicitness: int() is an explicit conversion, whereas eval() is an implicit execution of code.

(3) Flexibility: eval() can execture any valid python code, not just integer conversions.
'''

    



