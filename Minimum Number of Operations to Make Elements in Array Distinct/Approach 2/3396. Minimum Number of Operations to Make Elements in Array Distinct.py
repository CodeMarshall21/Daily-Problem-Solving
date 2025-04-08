class Solution:
    def minimumOperations(self,nums) -> int:
        unique = set()
        for num in range(len(nums)-1,-1,-1):
            if nums[num] in unique:
                return ((num // 3) + 1)
            unique.add(nums[num])
        return 0 
    