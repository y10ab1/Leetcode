class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*(m) for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                dp[i][j] = int(matrix[i][j])
                ans = max(dp[i][j], ans)
                
        
        for i in range(n-1):
            for j in range(m-1):
                LU = dp[i][j]
                LD = dp[i+1][j]
                RU = dp[i][j+1]
                RD = int(matrix[i+1][j+1])
                if RD == 1 and LU and LD and RU:
                    dp[i+1][j+1] = (min(LU,min(LD,RU))+1)
                ans = max(dp[i+1][j+1], ans)
                
        return ans**2