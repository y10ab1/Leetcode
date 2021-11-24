class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dis = (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
                heappush(edges,[dis,i,j])
        
        root = [i for i in range(len(points))]
        rank = [1 for _ in range(len(points))]
        ans = 0
        
        def find(idx):
            if root[idx] != idx:
                root[idx] = find(root[idx])
            return root[idx]
        
        def union(id1, id2):
            x, y = find(id1), find(id2)
            if rank[x] < rank[y]:
                root[x] = y
                rank[y] += rank[x]
            else:
                root[y] = x
                rank[x] += rank[y]
        
        
        while len(edges) > 0:
            e = heappop(edges)
            if find(e[1]) != find(e[2]):
                ans += e[0]
                union(e[1], e[2])
        return ans
                

            