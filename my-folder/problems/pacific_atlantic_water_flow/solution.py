class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        if not h or not h[0]:
            return []
        m,n = len(h), len(h[0])
        
        p_r = set()
        a_r = set()
        
        def dfs(x:int,y:int,r:set):
            if (x,y) in r:
                return
            r.add((x,y))
            for i,j in [(0,1),(0,-1),(-1,0),(1,0)]:
                if 0<=x+i<m and 0<=y+j<n:
                    if h[x+i][y+j] >= h[x][y]:
                        dfs(x+i,y+j,r)
        
        for r in range(m):
            dfs(r,0,p_r)
            dfs(r,n-1,a_r)
        for c in range(n):
            dfs(0,c,p_r)
            dfs(m-1,c,a_r)
        return list(p_r&a_r)
            