'''
Linear Time Complexity -> O(n)

Explanation: https://youtu.be/cWz4_zUegxE?si=rssboCGgIjzvXb__&t=182
 
'''

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        minimum = float('inf')
        cur_min = 0
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                cur_min += 1
            if right - left + 1 == k:
                minimum = min(cur_min,minimum)
                if blocks[left] == 'W':
                    cur_min -= 1
                left += 1
        return minimum
    
    