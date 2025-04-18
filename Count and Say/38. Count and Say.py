class Solution:
    def countAndSay(self, n: int) -> str:
        def counts(num):
            arr = []
            count = 1

            for i in range(1,len(num)):
                if num[i] == num[i-1]:
                    count += 1
                else:
                    arr.append(str(count)+num[i-1])
                    count = 1
            arr.append(str(count)+num[-1])
            return ''.join(arr)

        num = "1"
        for i in range(n - 1):
            num = counts(num)
        return num
    
    
'''
for better understanding 👇🏻

class Solution:
    def countAndSay(self, n: int) -> str:
        def counts (num):
            arr1 = []
            arr2 = [0] * 2
            arr2[1],arr2[0] = int(num[0]),1
            for i in range(1,len(num)):
                if num[i] == num[i - 1]:
                    arr2[0] += 1
                else:
                    arr1.append(arr2)
                    arr2 = [0] * 2
                    arr2[1],arr2[0] = int(num[i]),1
            arr1.append(arr2)
            val = ""
            for i in range(len(arr1)):
                val += str(arr1[i][0]) + str(arr1[i][1])
            return val
        
        if n == 1:
            return "1"
        num = "11"
        for i in range(n-2):
            num = counts(num)
        return num

'''