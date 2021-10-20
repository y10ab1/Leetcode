class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #RIGHT J++, I stay 0
        #DOWN J stay, I++ 1
        #LEFT J--, I stay 2
        #UP J stay, I-- 3
        
        fillcnt = 0
        state = 0
        J=-1;I=0
        a = [-1]*n
        ans = []
        for i in range(n):
            ans.append(a.copy())
        while fillcnt<n*n:
            if state == 0:
                if(J+1 == n or ans[I][J+1]!=-1):
                    state = (state+1)%4
                else:
                    fillcnt+=1;J+=1
                    ans[I][J] = fillcnt
            elif state == 1:
                if(I+1 == n or ans[I+1][J]!=-1):
                    state = (state+1)%4
                else:
                    fillcnt+=1;I+=1
                    ans[I][J] = fillcnt
            elif state == 2:
                if(J == 0 or ans[I][J-1]!=-1):
                    state = (state+1)%4
                else:
                    fillcnt+=1;J-=1
                    ans[I][J] = fillcnt
            elif state == 3:
                if(I == 0 or ans[I-1][J]!=-1):
                    state = (state+1)%4
                else:
                    fillcnt+=1;I-=1
                    ans[I][J] = fillcnt
        return ans
                
                
                