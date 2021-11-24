class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)
        
        
        # Build edges of the graph
        for idx, e in enumerate(equations):
            edges[e[0]].append((e[1], values[idx]))
            edges[e[1]].append((e[0], 1/values[idx]))

        def dfs(idx: str, target: str, val: float, seen: dict) -> float:
            seen[idx] = True
            res = -1.0
            if idx == target and edges[idx]:
                return val
            for e in edges[idx]:
                print(e)
                if not seen[e[0]]:
                    res = dfs(e[0], target, val*e[1], seen)
                    if res != -1.0:
                        return res
            return res
        
        ans = []
        for q in queries:
            seen = defaultdict(bool)
            ans.append(dfs(q[0], q[1], 1, seen))
        return ans
            