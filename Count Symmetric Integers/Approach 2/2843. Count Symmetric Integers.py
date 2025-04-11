class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        def isEqualSum(num):
            numStr = str(num)
            if len(numStr) % 2 == 0:
                left = 0
                right = len(numStr) - 1
                lsum = 0
                rsum = 0
                while (left < right):
                    lsum += int(numStr[left])
                    rsum += int(numStr[right])
                    left += 1
                    right -= 1
                return lsum == rsum
            else:
                return False
        
        for num in range(low,high+1):
            if (isEqualSum(num)):
                count += 1
        return count