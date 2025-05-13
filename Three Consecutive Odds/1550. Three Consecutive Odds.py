class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if (arr[i] & 1 != 0) and (arr[i + 1] & 1 != 0) and (arr[i + 2] & 1 != 0):
                return True
        return False