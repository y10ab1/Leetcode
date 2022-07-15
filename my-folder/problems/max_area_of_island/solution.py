class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 1
                    grid[i][j] = 0

                    for x,y in direction:
                        area += self.dfs(i+x,j+y,grid)
                    maxarea = max(maxarea, area)
                    
                        
        return maxarea
    
    def dfs(self, i, j, grid):
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j<0 or grid[i][j] != 1:
            return 0
        grid[i][j] = 0
        
        area = 1
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for x,y in direction:
            area += self.dfs(i+x, j+y, grid)
        
        
        return area
        