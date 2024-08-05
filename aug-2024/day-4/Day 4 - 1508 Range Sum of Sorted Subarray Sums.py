class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        summer = []
        mod = (10**9)+7
        # check = [1, 3, 6, 10, 2, 5, 9, 3, 7, 4]
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                summer.append(sum)
        # print(summer==check)
        
        # return summer
        summer.sort()
        # print(summer)
        new_sum = 0
        for i in range(left-1,right):
            # print(summer[i])
            new_sum += summer[i]
        
        return new_sum % mod