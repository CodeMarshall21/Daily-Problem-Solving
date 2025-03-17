class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        toggle = [False] * (max(nums)+1)
        for i in nums:
            toggle[i] = not toggle[i]
        
        return not any(toggle)