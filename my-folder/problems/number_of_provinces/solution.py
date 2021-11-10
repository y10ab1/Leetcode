class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        node = [0 for _ in range(len(isConnected))]
        cnt = 0
        def dfs(n):
            if node[n] != 0:
                return
            else:
                node[n] = cnt
            for idx,c in enumerate(isConnected[n]):
                if c == 1:
                    dfs(idx)
        
        for i in range(len(isConnected)):
            if node[i] == 0:
                cnt += 1
                dfs(i)
        return cnt
                    
                    
                    