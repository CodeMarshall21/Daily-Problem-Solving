def primeFinder(nums):

    primes = [True] * (max(nums)**2)
    primes[0] = primes[1] = False
    primesLen = len(primes)
    primeNums = []
    i = 2
    
    while(i*i < primesLen):
        if (primes[i]):
            for j in range(i*i,primesLen,i):
                primes[j] = False
        i += 1
    
    for num in range(primesLen):
        if (primes[num]):
            primeNums.append(num)

    return (primeNums[nums[0]-1] * primeNums[nums[1]-1]) - 1   
    


val = input().split()
nums = []
for i in val:
    if i != " ":
        nums.append(int(i))
        
print(primeFinder(nums))