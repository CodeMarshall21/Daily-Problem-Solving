class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majorityElement = 0
        count = 0

        # for n in nums:
        #     if count == 0:
        #         majorityElement = n
        #         count = 1
        #     elif n == majorityElement:
        #         count += 1
        #     else:
        #         count -= 1
        
        for n in nums:
            if count == 0:
                majorityElement = n
            if n == majorityElement:
                count += 1
            else:
                count -= 1


        leftCount = 0
        rightCount = nums.count(majorityElement)

        for i in range(len(nums)):
            if nums[i] == majorityElement:
                leftCount += 1
                rightCount -= 1
                
                leftLength = i + 1
                rightLength = len(nums) - leftLength

                if leftCount > (leftLength//2) and rightCount >  (rightLength//2) :
                    return i
        return -1
