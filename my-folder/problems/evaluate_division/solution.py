class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)
        for (a, b), v in zip(equations, values):
            edges[a].append((b, v))
            edges[b].append((a, 1/v))
            
        def dfs(A, B, seen):
            if seen[A]:
                return -1
            else:
                seen[A] = True
                for (nextNode, value) in edges[A]:
                    nextval = -1
                    if nextNode == B:
                        return value
                    
                    nextval = dfs(nextNode, B, seen)
                    if nextval == -1:
                        continue
                    else:
                        return nextval * value
                                                 
                return -1
            
        ansList = []
        
        for A, B in queries:
            seen = defaultdict(bool)
            ansList.append(dfs(A, B, seen))
        return ansList