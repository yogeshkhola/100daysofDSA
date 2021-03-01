array=[1,2,3,4,5]
shift=2

for i in range(0,shift):
    temp=array[0]

    for j in range(0,len(array)-1):
        array[j]=array[j+1]
    array[len(array)-1] =temp

for i in range (0,len(array)):
    print(array[i],end=" ")