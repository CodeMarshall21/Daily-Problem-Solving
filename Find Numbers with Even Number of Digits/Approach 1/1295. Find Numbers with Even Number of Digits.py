class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            stringLen = len(str(i))
            if stringLen % 2 == 0:
                count += 1
        return count