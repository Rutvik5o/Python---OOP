'''
(7)=> Write a program to find the sum of even number using
command line arguments
'''

import sys

n=int(sys.argv[1])
i=2
sum=0

while(i<=n):
    sum += i
    i += 2

print("Sum of even Number-> ",sum)

#if you run on IDLE -> Run on Customized
#if you run on cmd -> python filename.py number Ex: python seven.py 25