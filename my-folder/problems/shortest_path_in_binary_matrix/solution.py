class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        q = deque([])
        q.append([0,0,0])
        d = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
        while q:
            x,y,cnt = q.popleft()
            cnt += 1
            if x == len(grid)-1 and y == len(grid[0])-1:
                return cnt
            for way in d:
                nx = x+way[0]
                ny = y+way[1]
                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == 0:
                    q.append([nx,ny,cnt])
                    grid[nx][ny] = -1
        return -1
                
        