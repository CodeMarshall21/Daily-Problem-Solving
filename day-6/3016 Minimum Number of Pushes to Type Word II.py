class Solution:
    def minimumPushes(self, word: str) -> int:
            counts = [0]*26
            for char in word:
                counts[ord(char) - ord("a")] += 1
            counts.sort(reverse = True)
            
            
            i = 1
            count = 1
            sum = 0
            for j in range(len(counts)):
                sum = (counts[j]*i) + sum
                count += 1
                if count == 9:
                    count = 1
                    i += 1
            return sum
