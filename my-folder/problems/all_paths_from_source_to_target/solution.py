class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        tmp = []
        def dfs(n):
            
            tmp.append(n)
            if n == len(graph)-1:
                ans.append(tmp.copy())
                tmp.pop()
                return
            for i in graph[n]:
                dfs(i)
            tmp.pop()
        dfs(0)
        return ans