class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # sort by x-coord
        
        # checkpoints
        cp = [(l,-h,r) for l,r,h in buildings] + list(set((r,0,0) for _,r,_ in buildings))
        cp.sort()
        hp = [(0,float('inf'))]
        res = [[0,0]]
        for l,h,r in cp:
            while l >= hp[0][1]:heapq.heappop(hp)
            if h :heapq.heappush(hp,(h,r))
            if res[-1][1] != -hp[0][0]: res.append((l,-hp[0][0]))
        
        return res[1:]