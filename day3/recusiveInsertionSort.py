#recursive insertion sort

def insertRecursive(array,n):
    if n <= 1:
        return

    insertRecursive(array,n-1)
    last=array[n-1]
    j=n-2
    while (j>0 and array [j]>last):
        array [j+1]=array[j]
        j=j-1
    array[j+1]=last

array=[1,5,3,74,4,5,2]
n=len(array)
insertRecursive(array,n)

for i in range(n):
    print(array[i],end=" ")