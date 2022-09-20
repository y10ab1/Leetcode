class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:

        # n,m = len(nums1),len(nums2)
        # dp = [[0]*(m+1) for _ in range(2)]
        # ans = 0
        # for i in range(1,n+1):
        #     for j in range(1,m+1):
        #         if nums1[i-1] == nums2[j-1]:
        #             dp[1][j] = dp[0][j-1]+1
        #         else:
        #             dp[1][j] = 0
        #         ans = max(ans, dp[1][j])
        #     dp[1],dp[0] = dp[0],dp[1]
        # return ans
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)
        
        
        