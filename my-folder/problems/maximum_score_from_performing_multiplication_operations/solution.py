class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        
        dp = [[0]*(m+1) for _ in range(m+1)]
        
        for i in range(m-1,-1,-1):
            for j in range(i,-1,-1):
                mul = multipliers[i]
                l_n = nums[j]
                r_n = nums[n-1-(i-j)]
                dp[i][j] = max(l_n*mul+dp[i+1][j+1], r_n*mul+dp[i+1][j])
        return dp[0][0]