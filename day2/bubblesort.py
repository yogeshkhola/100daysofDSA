#sorting using bubble sortion

def sort(nums):
    for i in range(len(nums)-1,0,-1):#reduce one element in each iteration 
        for j in range(i):
            if nums[j]>nums[j+1]:

                temp=nums[j]   #swapping
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums=[5,3,8,6,7,2]
sort(nums)

print(nums)