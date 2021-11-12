class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        
        
        q = deque([start])
        seen = set([start])
        
        while q:
            node = q.popleft()
            if node == end:
                return True
            else:
                for n in d[node]:
                    if not n in seen:
                        q.append(n)
                        seen.add(n)
        return False
                
        
        
        