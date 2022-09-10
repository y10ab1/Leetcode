class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*2 for _ in range(k+1) ] for _ in range(n+1)] # dp[i][k][hold]
        
        for i in range(n-1,-1,-1):
            for trans in range(1,k+1):
                for hold in range(2):
                    
                    do_nothing = dp[i+1][trans][hold]
                    
                    if hold:
                        # sell
                        do_sthing = prices[i] + dp[i+1][trans-1][0]
                    else:
                        # buy
                        do_sthing = -prices[i] + dp[i+1][trans][1]
                    
                    dp[i][trans][hold] = max(do_nothing, do_sthing)
        
        return dp[0][k][0]
                    