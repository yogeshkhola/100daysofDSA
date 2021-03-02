#sorting using insertion sort  method

array=[4,1,7,5,15,11,55,40]

for i in range(1,len(array)):#start iterating with 2nd element
    current_value=array[i] #variable store current value
    position=i #pointer
    while(position>0 and array[position-1]>current_value):
        array[position]=array[position-1]
        position=position-1#previous elements compare
    array[position]=current_value

print(array)

