'''
Topic -> Sliding Window 
Explanation -> https://youtu.be/Zexx16dNPX8?si=am1laGN3rxxd4ZrX

'''


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        left = 0
        count = 0
        for right in range(1,n+k-1):
            if colors[right % n] == colors[(right - 1) % n]:
                left = right
            if right - left + 1 > k:
                left += 1
            if right - left + 1 == k:
                count += 1
        return count