class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        edges = defaultdict(list)
        root = -1
        for p, pp in zip(pid,ppid):
            edges[pp].append(p)
            if pp == 0:
                root = p
        ans = []
        
        def dfs(idx:int,ischild:bool)->List[int]:
            if ischild:
                ans.append(idx)
            for e in edges[idx]:
                dfs(e,e==kill or ischild)
                
        dfs(root, root==kill)
        return ans
                