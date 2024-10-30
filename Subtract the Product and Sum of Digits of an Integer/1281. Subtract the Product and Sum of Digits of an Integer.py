class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return (prod(int(j) for j in str(n))-sum((int(j) for j in str(n))))