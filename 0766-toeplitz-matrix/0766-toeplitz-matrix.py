class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n,m = len(matrix), len(matrix[0])
        # (n-1,0) ~ (0,0)
        # (0,1) ~ (0,m-1)
        for i in range(n-1,-1,-1):
            j = 0
            pre = matrix[i][j]
            while 0<=i+1<n and 0<=j+1<m:
                if matrix[i+1][j+1]!=pre:
                    return False
                pre = matrix[i+1][j+1]
                j+=1
                i+=1
        for j in range(1,m):
            i = 0
            pre = matrix[i][j]
            while 0<=i+1<n and 0<=j+1<m:
                if matrix[i+1][j+1]!=pre:
                    return False
                pre = matrix[i+1][j+1]
                j+=1
                i+=1
        return True