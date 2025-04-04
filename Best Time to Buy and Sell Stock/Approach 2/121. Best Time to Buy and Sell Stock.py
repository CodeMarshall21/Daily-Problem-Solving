class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            profit= prices[i]-min_price
            max_profit= max(profit,max_profit)
        return max_profit