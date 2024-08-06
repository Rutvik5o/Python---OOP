'''
(22)=> Write a program to convert the elements of two list into key value 
pairs of a dictionary
'''


index = [1,2,3]
languages = ['Python','C++','Java']

dictionary = dict(zip(index,languages))

print(dictionary)