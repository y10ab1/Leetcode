class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        #dp[dice][sum of total]
        #dp[i][j] = dp[i-1]
        
        dp = [[0]*(1000+1) for _ in range(n+1)]
        for i in range(1,k+1):
            dp[1][i]=1
        for i in range(2,n+1):
            for j in range(min(dp[i-1]),target+1):
                for kk in range(1,k+1):
                    dp[i][j] += dp[i-1][j-kk]
        return dp[n][target] %(10**9+7)
                