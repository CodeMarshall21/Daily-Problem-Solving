class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashtable = {}
        res = []
        sums = 0
        for i in range (len(grid)):
            for j in range (len(grid[i])):
                sums += grid[i][j]
                hashtable[grid[i][j]] = hashtable.get((grid[i][j]),0) + 1
                if (hashtable[grid[i][j]]) > 1:
                    res.append(grid[i][j])
                    sums -= grid[i][j]
        # print(hashtable)
        # print(res) 
        act_sum = sum(k for k in range((len(grid)*len(grid[0]))+1))
        
        res.append(act_sum-sums)

        return res


