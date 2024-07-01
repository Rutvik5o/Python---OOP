#(4)=> Write a program to sort the array elements using bubble sort techniques.

def bubblesort(arr):

    n=len(arr)

    for i in range(n-1):

        for j in range(0,n-i-1):

            if arr[j]>arr[j+1]:

                arr[j],arr[j+1]=arr[j+1],arr[j]


            
arr=[46,36,73,994,22,3]

bubblesort(arr)

print("Sorted Array")

for i in arr:
    print(i)
