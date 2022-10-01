class Solution:
    def numDecodings(self, s: str) -> int:
        cur,p,pp=0,1,1
        s = [int(c) for c in s]
        for i in range(len(s)):
            if s[i] != 0: cur+=p
            if i>0 and (s[i-1]==1 or s[i-1]==2 and s[i]<7):
                cur+=pp
            pp,p,cur=p,cur,0
        return p