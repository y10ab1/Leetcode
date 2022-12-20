class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        s = set()
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        
        def dfs(node):
            s.add(node)
            for i in d[node]:
                if i not in s:
                    dfs(i)
        ans = 0
        for i in range(n):
            if i not in s:
                dfs(i)
                ans+=1
        return ans