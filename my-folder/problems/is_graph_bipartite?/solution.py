class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = [0] * len(graph)
        
        def dfs(node):
            for n in graph[node]:
                if seen[n] == seen[node] * -1:
                    continue
                elif seen[n] == seen[node]:
                    return False
                else:
                    seen[n] = seen[node] * -1
                    if not dfs(n):
                        return False
            return True
        
        
        for i in range(len(graph)):
            if seen[i] == 0:
                seen[i] = 1
                if not dfs(i):
                    return False
        return True