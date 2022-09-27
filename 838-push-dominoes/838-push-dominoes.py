class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # . before L -> L
        # . between R and L -> RR...LL
        # . between L and R -> .
        # . after R -> R
        dominoes = [c for c in dominoes]
        LR = [(i,c) for i,c in enumerate(dominoes) if c != '.']
        

        preidx,j,prec =0,0,'L'
        for idx,c in LR:
            if c == 'L' and prec == 'L':
                for k in range(idx-1,-1,-1):
                    if dominoes[k]=='.':
                        dominoes[k]='L'
                    else:
                        break
                        
            elif c == 'L' and prec == 'R':
                m = (idx-preidx-1)//2
                for k in range(idx-1,idx-m-1,-1):
                    dominoes[k] = 'L'
                if (idx-preidx-1)%2==1:
                    dominoes[idx-m-1] = '.'
            elif c == 'R':
                for k in range(idx+1,len(dominoes)):
                    if dominoes[k] == '.':
                        dominoes[k] = 'R'
                    else:
                        break
            
            preidx,prec = idx,c
            
            
        return "".join(dominoes)
                