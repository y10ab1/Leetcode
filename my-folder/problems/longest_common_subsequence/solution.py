class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        if n<m:
            n,m=m,n
            text1,text2=text2,text1
            
        dp = [[0]*(m+1) for _ in range(2)]
        curmax, premax = 0, 0
        
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[1][j] = dp[0][j-1]+1
                else:
                    dp[1][j] = max(dp[1][j-1], dp[0][j])
            dp[0],dp[1]=dp[1],dp[0]
        
        return dp[0][-1]