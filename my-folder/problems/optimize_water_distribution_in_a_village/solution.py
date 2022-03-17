class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edge = []
        totalCost = 0
        self.root = [x for x in range(n+1)]
        
        for h1, h2, cost in pipes:
            edge.append((cost,h1,h2))
        
        for h in range(1,n+1):
            edge.append((wells[h-1],h,0))
        
        edge.sort()
        
        for cost, h1, h2 in edge:
            if self.find(h1) != self.find(h2):
                totalCost += cost
                self.union(h1,h2)
        
        
        return totalCost
    
    def find(self, idx):
        if self.root[idx] != idx:
            self.root[idx] = self.find(self.root[idx])
        return self.root[idx]
        
    def union(self, id1, id2):
        self.root[self.find(id1)] = self.find(id2)