class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [set() for _ in range(n)]
        if len(adj) == 1:
            return [0]
        
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        
        leaves = [x for x in range(n) if len(adj[x]) == 1]
        print(leaves)
        
        while n > 2:
            n -= len(leaves)
            
            newleaves = []
            for node in leaves:
                x = adj[node].pop()
                adj[x].remove(node)
                
                if len(adj[x])==1:
                    newleaves.append(x)
            leaves = newleaves
    
        
        return leaves
            