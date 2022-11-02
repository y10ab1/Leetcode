class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        n,m = len(grid), len(grid[0])
        for col in range(m):
            row = 0
            while row < n:
                if grid[row][col] == 1 and col+1 < m and grid[row][col+1] == 1:
                    row,col=row+1,col+1              
                elif grid[row][col] == -1 and 0<=col-1 and grid[row][col-1] == -1:
                    row,col=row+1,col-1
                else:
                    ans.append(-1)
                    break
            if row == n:
                ans.append(col)
        return ans
            
                