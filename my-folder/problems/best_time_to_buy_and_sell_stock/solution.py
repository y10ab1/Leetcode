class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur, maxp = float('inf'), 0
        for i in range(len(prices)):
            if cur >= prices[i]:
                cur = prices[i]
            else:
                maxp = max(maxp, prices[i]-cur)
        return maxp