class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxNum = 0
        maximum = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]
            for k in range(i+1,len(nums)):
                maxNum = max(maxNum,(maximum - nums[i])*nums[k])
        return maxNum
