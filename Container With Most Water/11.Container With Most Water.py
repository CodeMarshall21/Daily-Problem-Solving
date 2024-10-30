class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force <- efficient illa O(n**2)!!!
        # max_cap = 0
        # for i in range(len(height)):
        #     count = 0
        #     for j in range(i,len(height)):
        #         curr_height = min(height[i],height[j])
        #         area = curr_height * count
        #         max_cap = max(area,max_cap)
        #         count += 1
        # return max_cap

        left = 0
        right = len(height) - 1
        lenght = len(height) - 1
        max_cap = 0

        while left != right:
            min_height = min(height[left], height[right])
            area = min_height * lenght
            lenght -= 1
            max_cap = max(area,max_cap)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_cap