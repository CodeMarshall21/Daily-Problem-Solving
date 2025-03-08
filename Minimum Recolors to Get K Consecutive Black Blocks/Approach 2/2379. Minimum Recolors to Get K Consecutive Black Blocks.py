class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum = float('inf')
        left = 0
        right = k

        while right <= len(blocks):
            curr_str = blocks[left:right]
            cur_min = curr_str.count('W')
            minimum = min(cur_min,minimum)
            left += 1
            right += 1

        return minimum