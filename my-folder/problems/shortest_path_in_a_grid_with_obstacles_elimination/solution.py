class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n,m = len(grid),len(grid[0])
        if n==m and n==1:
            return 0
        q = deque([(0,0,k,0)])
        s = set((0,0,k))
        
        while q:
            d = [(1,0),(0,1),(-1,0),(0,-1)]
            i,j,quota,step = q.popleft()
            for x,y in d:
                if 0<=i+x<n and 0<=j+y<m and grid[i+x][j+y] == 1 and quota > 0 and not (i+x,j+y,quota-1) in s:
                    q.append((i+x,j+y,quota-1,step+1))
                    s.add((i+x,j+y,quota-1))
                if 0<=i+x<n and 0<=j+y<m and grid[i+x][j+y] == 0 and not (i+x,j+y,quota) in s:
                    if i+x == n-1 and j+y == m-1:
                        return step+1
                    q.append((i+x,j+y,quota,step+1))
                    s.add((i+x,j+y,quota))
        return -1