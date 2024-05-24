def bubble(nums):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums
nums=[10,40,5,6,80,25,457]
print(bubble(nums))