class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # if exist a path that END = DESTINATION ->　False
        # self loop -> false
        # no path to destination -> false
        
        de = defaultdict(list)
        seen = defaultdict(bool)
        for e in edges:
            de[e[0]].append(e[1])
            
        def dfs(idx):
            if de[idx] == [] and idx != destination:
                return False
            seen[idx] = True
            for n in de[idx]:
                if seen[n]:
                    return False
                if not dfs(n):
                    return False
            seen[idx] = False
            return True
        
        return dfs(source)
            