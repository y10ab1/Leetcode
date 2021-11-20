class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        logs.sort()
        u = [i for i in range(n)]
        r = [1 for _ in range(n)]
        c = n
        
        def find(idx):
            while u[idx] != u[u[idx]]:
                u[idx] = u[u[idx]]
            return u[idx]
        for t,i,j in logs:
            x, y = find(i), find(j)
            if x != y:
                if r[i] >= r[j]:
                    u[y] = x
                    r[i] += 1
                else:
                    u[x] = y
                    r[j] += 1
                c-=1
            if c == 1:
                return t
            
        return -1