class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycle
        # connected
        d = {}
        d_e = defaultdict(list)
        for e in edges:
            d_e[e[0]].append(e[1])
            d_e[e[1]].append(e[0])
            
        def dfs(idx, root):
            if d.get(idx):
                return False
            
            d[idx] = root
            for n in d_e[idx]:
                if n == root:
                    continue
                if not dfs(n, idx):
                    return False
            return True
        
        OK = dfs(0,-1)
        if OK:
            for i in range(n):
                if not d.get(i) and d.get(i) != 0:
                    return False
        return  OK
            
            
        