class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window_size = sum(nums)
        length = len(nums)
        left = 0
        ones = 0
        max_ones = 0
        min_swaps = 0
        for right in range(2*length):
            if nums[right%length] == 1:
                ones += 1
            if right - left + 1 > window_size:
                ones -= nums[left%length]
                left += 1
            max_ones = max(ones,max_ones)
        min_swaps = window_size - max_ones

        return min_swaps