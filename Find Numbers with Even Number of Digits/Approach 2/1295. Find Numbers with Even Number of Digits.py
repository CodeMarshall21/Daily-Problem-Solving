class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def hasEvenDigit(num):
            digitCount = 0
            while(num > 0):
                digitCount += 1
                num = num//10
            return digitCount & 1 == 0 # to ckeck if even '&' with 1

        count = 0
        for i in nums:
            if (hasEvenDigit(i)):
                count += 1
        return count