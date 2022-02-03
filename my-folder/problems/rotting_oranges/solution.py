class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        freshCnt = 0
        m, n = len(grid), len(grid[0])
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshCnt+=1
                if grid[i][j] == 2:
                    q.append((i,j))
        
        while q and (freshCnt != 0):
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    x, y = i+dx, j+dy
                    if x<0 or y<0 or x==m or y==n or grid[x][y]!=1:
                        continue

                    grid[x][y] = 2
                    q.append((x,y))
                    freshCnt-=1
            time+=1
                
                    
            
        if freshCnt != 0:
            return -1
        else:
            return time