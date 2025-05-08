class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        def hashfunction(domino):
            key = ""
            domino.sort()
            key += str(domino[0]) + str(domino[1])
            return key
        hashmap = {}
        pairs = 0
        for domino in dominoes:
            key = hashfunction(domino)
            # print(key)
            hashmap[key] = hashmap.get(key,0) + 1
        # print(hashmap)
        for keys in hashmap:
            n = hashmap[keys]
            pairs += n * (n - 1)//2
        return pairs