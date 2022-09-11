class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit, l = 0, 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                maxprofit = max(maxprofit, prices[r]-prices[l])
            else:
                l = r
        return maxprofit