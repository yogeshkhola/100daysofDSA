# Python program for array rotation(left shift) by d elements

arr=[1,2,3,4,5,6,7]

# function to left rotate the array[] of size n by d
def leftRotate(arr,d,n):
    for i in range(d):
        leftRotatebyOne(arr,n)

#function to left rotate arr[] by size 1

def leftRotatebyOne(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]

    arr[n-1]=temp

def printarray(arr,size):
    for i in range(size):
        print(" %d" % arr[i],end="")

leftRotate(arr,2,7)
printarray(arr,7)