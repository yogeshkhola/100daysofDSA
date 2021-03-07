pos=-1

def binarysearch(list,key):
    low=0
    high=len(list)-1
    found=False

    while low<=high and not found:
        mid=(low+high)//2
        if key==list[mid]:
            globals () ['pos']=mid
            found=True
        elif key>list[mid]:
            low=mid+1
        else:
            high=mid-1

    if found==True:
        print("key is found at:",pos+1)
    else:
        print("key is not found")

list=[24,7,9,21,13]
list.sort()
print(list)
key=int(input("enter the key"))
binarysearch(list,key)