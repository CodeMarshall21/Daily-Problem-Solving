def bestDay(days):
    maxProfit = 0
    
    for i in range(1,len(days)):
        for j in range(i,len(days)):
            currProfit = days[j] - days[i]
            maxProfit = max(currProfit,maxProfit)
    return maxProfit

days = list(map(int, input().split()))

print(bestDay(days))
            