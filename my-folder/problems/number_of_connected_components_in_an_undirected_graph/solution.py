class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = [0 for _ in range(n)]
        de = defaultdict(list) #dict of edges
        for e in edges:
            de[e[0]].append(e[1])
            de[e[1]].append(e[0])
        def dfs(idx):
            seen[idx] = 1
            for n in de[idx]:
                if seen[n]:
                    continue
                dfs(n)
        cnt = 0
        for i in range(n):
            if seen[i] == 0:
                cnt += 1
                dfs(i)
        return cnt