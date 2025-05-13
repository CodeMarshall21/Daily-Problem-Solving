class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        digitHashmap = Counter(digits)
        for i in range(100,1000,2):
            numberHashmap = Counter([int(j) for j in str(i)])
            flag = 0
            for k in numberHashmap.keys():
                if numberHashmap[k] > digitHashmap[k]:
                    flag = 1
            if flag == 0:
                ans.append(i)
        return ans