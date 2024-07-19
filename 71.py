#(1)=>Write a programto handle some built in exceptions like ZeroDivisonError.

a=int(input("Enter a dividend->"))

b=int(input("Enter a divisor->"))

try: 
    Ans=a/b

except ZeroDivisionError:
    print("Can't Divide by zero")

else:
    print("Answer=>",Ans)


#else block=> if there is no exception in try block then try & else both block will be executed.

#except block=> if any exception found on try block then only except block will be executed.
