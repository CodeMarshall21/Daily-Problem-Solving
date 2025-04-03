def maxProduct(nums):
    SortedNums = nums.sort()
    prod1 = nums[0] * nums[1]
    prod2 = nums[len(nums)-1] * nums[len(nums)-2]
    
    return [nums[0],nums[1]] if (prod1 > prod2) else  [nums[len(nums)-1], nums[len(nums)-2]] 
    
    # return res
nums = [-216,-154,23,2,65]
print(maxProduct(nums))