# Given an array arr of n positive integers, your task is to find all the leaders in the array. 
# An element of the array is considered a leader if it is greater than all the elements on its right side or if it is equal to the maximum element on its right side. 
# The rightmost element is always a leader.

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        #Code here
        res = []
        high = arr[-1]
        
        # res.append(high)
        
        for i in range(n-2,-1,-1):
            if arr[i] >= high:
                res.append(high)
                high = arr[i]
        res.append(high)
        
        return reversed(res)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(N, A)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends