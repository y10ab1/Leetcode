class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        e = defaultdict(list)
        v = [0 for _ in range(n)]
        for i in edges:
            e[i[0]].append(i[1])
            e[i[1]].append(i[0])
        def dfs(s):
            v[s] = 1
            if s == end:
                return True
            for i in e[s]:
                if v[i] == 0 and dfs(i):
                    return True
            return False
        return dfs(start)