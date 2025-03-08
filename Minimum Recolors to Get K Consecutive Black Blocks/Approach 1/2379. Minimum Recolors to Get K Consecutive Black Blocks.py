#Sliding Window


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum = float('inf')
        left = 0
        right = k
        while right <= len(blocks):
            cur_min = 0
            for i in range (left,right):
                if blocks[i] == 'W':
                    cur_min += 1
            minimum = min(cur_min, minimum)
            left += 1
            right += 1
        return minimum