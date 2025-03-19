class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range (len(nums)-2):
            if nums[i] == 0:
                nums[i], nums[i+1], nums[i+2] = 1, 1^nums[i+1], 1^nums[i+2]
                count += 1
            
        if ((nums[len(nums)-1] == 1) and  (nums[len(nums)-2] == 1) and (nums[len(nums)-3] == 1)):
            return count
        else:
            return -1
        
