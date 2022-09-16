class Solution:
    def maximumScore(self, nums: List[int], mul: List[int]) -> int:
        n, m = len(nums), len(mul)
        dp = [[0]*(m+1) for _ in range(m+1)]
        
        # l -> left index of nums, r -> right index of nums
        # k -> index of mul
        # dp[k][l] = max(nums[l]*mul[k]+dp[l+1][k+1], nums[r]*mul[k]+dp[l][k+1])
        
        for k in range(m-1,-1,-1):
            for l in range(k,-1,-1):
                r = n-1-(k-l)
                dp[k][l] = max(nums[l]*mul[k]+dp[k+1][l+1], nums[r]*mul[k]+dp[k+1][l])
        
        return dp[0][0]