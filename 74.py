#(4)=> write a program to provide a function for making file lists from directorry wildcard searrches:

import os

def findfiles(filename,searchpath):

    result=[]

    for root,dir,files in os.walk(searchpath):

        if filename in files:

            result.append(os.path.join(root,filename))


        if result == []:

            return("No Such file found")
        
        else:

             return result
        

    
name=input("Enter Filename with extension for file creation->")

f=open(name,'w')

f.close()


file=input("Enter filename with extension for searching->")
print(findfiles(file,os.getcwd()))