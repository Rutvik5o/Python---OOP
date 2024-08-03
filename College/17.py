'''
(7)=> Write a python program that removes any repeated items from a list so that
each item appears at most once. for instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0]
'''


def rename(duplicate):

    final_list=[]

    for num in duplicate:

        if num not in final_list:

            final_list.append(num)
        
    return final_list

print("Removing Duplicate Elements=>",rename([43,34,34,342,52,2,43,31,2]))