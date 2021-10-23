class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt=1     
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i,j,grid,cnt)
                    cnt+=1
        return cnt-1
    
    
    def dfs(self,i,j,grid,cnt):
        if i < 0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            
            return
        grid[i][j] = cnt
        self.dfs(i-1,j,grid,cnt)
        self.dfs(i+1,j,grid,cnt)
        self.dfs(i,j-1,grid,cnt)
        self.dfs(i,j+1,grid,cnt)