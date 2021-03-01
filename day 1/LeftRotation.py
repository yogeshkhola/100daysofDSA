# Python implementation of left rotation of an array k times

def leftRotate(arr, n, k):  # functioon to leftRotate array[] no. of times
    k = k % n
    for i in range(n):
        print(str(arr[(k + i) % n]), end=" ")  # print rotated array


arr = [1, 3, 5, 7, 9]
n = len(arr)

k = 2
leftRotate(arr, n, k)  # function call

print(" ")

k = 3
leftRotate(arr, n, k)  # function call

print("")

k = 4
leftRotate(arr, n, k)  # function call

