class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_map = {}
        for char in arr:
            hash_map[char] = hash_map.get(char, 0) + 1
        
        for i in hash_map:
            if hash_map[i] == 1:
                k -= 1
                if k == 0:
                    return i
            
        return ""