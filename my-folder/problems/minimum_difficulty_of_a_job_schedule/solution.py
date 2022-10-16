class Solution:
    def minDifficulty(self, jobD: List[int], d: int) -> int:
        n = len(jobD)
        if n < d:
            return -1
        
        # dp[i][k] is min difficulty when doing i'th job at k'th day
        
        @lru_cache(None)
        def dp(i,k):
            # leftjobs = n-i-1
            # leftdays = d-k-1
            if k==d-1:
                return max(jobD[i:])
            hardest = 0
            ret = float('inf')
            for jid in range(i,n-d+k+1):
                hardest = max(jobD[jid],hardest)
                ret = min(ret, hardest + dp(jid+1,k+1))
            return ret
        return dp(0,0)
        