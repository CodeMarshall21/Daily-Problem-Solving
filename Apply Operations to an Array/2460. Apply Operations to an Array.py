
'''
'''



def applyOperations(nums):
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i + 1] = 0
        i = 0
        j = 0
        while(j!=len(nums)):
            if (nums[j] != 0):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
            j += 1 
        return nums
     
nums = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
   
print(applyOperations(nums))

