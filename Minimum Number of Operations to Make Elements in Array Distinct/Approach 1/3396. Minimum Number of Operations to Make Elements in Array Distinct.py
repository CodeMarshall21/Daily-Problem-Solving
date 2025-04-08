class Solution:
    def minimumOperations(self,nums):
        times = 0
        while len(nums) != len(set(nums)):
            times += 1
            nums = nums[3:]
        return times

