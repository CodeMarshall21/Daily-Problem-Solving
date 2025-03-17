class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        if len(nums) % 2 != 0:
            return False
        
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1

        print(hashmap)

        for key in hashmap:
            if hashmap[key] % 2 != 0:
                return False
        return True