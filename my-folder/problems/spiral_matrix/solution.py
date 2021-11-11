class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        Dx, Dy = d[0]
        i, j = 0, 0
        cnt = 0
        ans = []
        def check(a,b):
            if a >= m or a < 0 or b < 0 or b >= n or matrix[a][b] == None:
                return False
            else:
                return True
        while len(ans) < m*n:
            ans.append(matrix[i][j])
            matrix[i][j] = None
            if not check(i+Dx,j+Dy):
                cnt += 1
            Dx, Dy = d[cnt%4]                
            i += Dx
            j += Dy
        return ans
            
        