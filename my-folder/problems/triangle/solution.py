class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle.copy()
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] += triangle[i-1][j-1]
                else:
                    dp[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        
        return min(dp[-1])
        
        