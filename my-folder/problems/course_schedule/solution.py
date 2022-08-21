class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        edge, seen = defaultdict(list), defaultdict(bool)
        innode = defaultdict(int)
        for target, req in p:
            edge[req].append(target)
            innode[target] += 1
        q = deque([])
        
        for i in range(n):
            if innode[i] == 0:
                q.append(i)

        while q:
            qn = len(q)
            for _ in range(qn):
                node = q.popleft()
                for e in edge[node]:
                    innode[e] -= 1
                    if innode[e] == 0:
                        q.append(e)
                    
        for i in range(n):
            if innode[i] != 0:
                return False
        return True
                
        