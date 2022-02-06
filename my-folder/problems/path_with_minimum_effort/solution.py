class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        cost = [(0,0,0)]
        maxCost = 0
        m, n = len(heights), len(heights[0])
        seen = defaultdict(bool)
        while cost:
            c, i, j = heapq.heappop(cost)
            seen[(i,j)] = True
            maxCost = max(c, maxCost)
            if (i,j) == (m-1,n-1):
                return maxCost
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                x, y = dx+i, dy+j
                if x<0 or y<0 or x>=m or y>=n or seen[(x,y)]:
                    continue
                heapq.heappush(cost, (abs(heights[i][j] - heights[x][y]), x, y))
        
                    