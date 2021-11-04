class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                #i+1
                if c == i:
                    dp[i] = 1
                    break
                elif i > c:
                    dp[i] = min(dp[i-c]+1, dp[i])
        if dp[amount] != amount+1 :
            return dp[amount]
        else:
            return -1
            