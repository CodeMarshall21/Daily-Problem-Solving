class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            numStr = str(num)
            numStr_len = len(numStr) 
            if numStr_len % 2 == 0:
                if sum(int(val) for val in numStr[:numStr_len // 2]) == sum(int(val) for val in numStr[numStr_len // 2:]):
                    count += 1
        return count