'''
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 3^1 + 3^2
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 3^0 + 3^2 + 3^4
Example 3:

Input: n = 21
Output: false
'''


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 0:
            return True
        rem = n % 3
        if rem == 2:
            return False
        return self.checkPowersOfThree(n // 3)