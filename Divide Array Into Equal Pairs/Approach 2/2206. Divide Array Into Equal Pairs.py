class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        unique = set()

        for i in nums:
            if i in unique:
                unique.remove(i)
            else:
                unique.add(i)
        
        return (not unique)