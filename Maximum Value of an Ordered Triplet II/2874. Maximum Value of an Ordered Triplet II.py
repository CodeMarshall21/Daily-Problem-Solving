class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefixMax = nums[0]
        maxDiff = 0
        res = 0
        for k in range(1,len(nums)):
            res = max(res, maxDiff * nums[k])
            maxDiff = max(maxDiff, prefixMax - nums[k])
            prefixMax = max(prefixMax, nums[k])
        return res