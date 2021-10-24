class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(now,l,r):
            if r > l:
                return
            elif l == n:
                for _ in range(n-r):
                    now+=')'
                ans.append(now)
                return
            else:
                dfs(now+'(',l+1,r)
                dfs(now+')',l,r+1)
            
                
                
        lcnt, rcnt = 1, 0
        dfs('(',lcnt,rcnt)
        return ans