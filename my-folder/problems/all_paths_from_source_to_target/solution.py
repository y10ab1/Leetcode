class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for idx,e in enumerate(graph):
            d[idx]+=e
        q = deque([[0]])
        ans = []
        while q:
            path = q.popleft()
            node = path[-1]
            for v in d[node]:
                temp_path = path.copy()
                temp_path.append(v)
                if v == len(graph) - 1:
                    ans.append(temp_path)
                else:
                    q.append(temp_path)
        
            
                
        return ans
                