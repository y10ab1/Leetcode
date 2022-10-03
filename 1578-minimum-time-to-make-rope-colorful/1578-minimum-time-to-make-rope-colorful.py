class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        colors = [c for c in colors]
        q = [('A',0)]
        ans = 0
        for i,c in enumerate(colors):
            if c == q[-1][0]:
                if q[-1][1] > neededTime[i]:
                    ans+=neededTime[i]
                else:
                    ans+=q.pop()[1]
                    q.append((c,neededTime[i]))
            else:
                q.append((c,neededTime[i]))
                
        return ans
                    
                    
                
        
            