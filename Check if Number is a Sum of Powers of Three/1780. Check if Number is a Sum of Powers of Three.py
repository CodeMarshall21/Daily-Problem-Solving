'''

'''


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 0:
            return True
        rem = n % 3
        if rem == 2:
            return False
        return self.checkPowersOfThree(n // 3)