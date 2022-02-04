class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        p, c = defaultdict(int), defaultdict(int)
        toFrom = defaultdict(list)
        for i in range(n):
            p[i] = float('inf')
            c[i] = float('inf')
        p[src] = 0
        c[src] = 0
            
        for f, t, w in flights:
            toFrom[t].append((f,w))
            
        for t in range(k+1): #from 1 to n-1
            for node in range(n):
                pair = toFrom[node]
                for f,w in pair:
                    if w+p[f] < c[node]:
                        c[node] = w+p[f]
            for i in c:
                p[i] = c[i]
        
        
        
        
        return c[dst] if c[dst] != float('inf') else -1
            