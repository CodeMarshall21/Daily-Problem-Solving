class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        greaterthanK = set()
        count = 0
        for val in nums:
            if val < k:
                return -1
            if val > k and val not in greaterthanK:
                greaterthanK.add(val)
                count += 1
        return count