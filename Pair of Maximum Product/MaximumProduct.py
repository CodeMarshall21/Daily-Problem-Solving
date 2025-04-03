def maxProduct(nums,maxProd):

    res = []
    for i in range(len(nums)):
        prod = 0
        for j in range(i+1,len(nums)):
            prod = nums[i] * nums[j]
            if prod == maxProd:
                res.append((nums[i],nums[j]))
    return res
nums = [8,8,2,32,4,16,5,3]
print(maxProduct(nums,64))