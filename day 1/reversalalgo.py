# Python program for reversal algorithm of array rotation

a = [1, 2, 3, 4, 5, 6, 7, 8]


def reverse_array(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1


reverse_array(a, 0, 1)
reverse_array(a, 2, 7)
reverse_array(a, 0, 7)
print(a)