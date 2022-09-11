class Solution:
    def partitionString(self, ss: str) -> int:
        l = [c for c in ss]
        cnt = len(ss)
        i = 1
        gid = 0
        s = set(l[0])
        
        while i < len(ss):
            if l[i] not in s:
                s.add(l[i])
                cnt-=1
            else:
                s = set(l[i])
            i+=1
        return cnt
                
                