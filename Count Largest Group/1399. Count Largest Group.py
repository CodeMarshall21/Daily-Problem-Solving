class Solution:
    def countLargestGroup(self, n: int) -> int:
        if (n // 10) == 0:
            return n
        hashTable = {}
        def digitSum(num):
            sums = 0
            while num > 0:
                sums += num % 10
                num = num // 10
            return sums
        for i in range(1,n+1):
            digitsum = digitSum(i)
            hashTable[digitsum] = hashTable.get(digitsum, 0) + 1
        maxVal = max(hashTable.values())
        count = 0
        for values in hashTable.values():
            if values == maxVal:
                count += 1
        return count