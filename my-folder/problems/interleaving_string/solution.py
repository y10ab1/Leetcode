class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        
        lastdp, curdp = [False] * (len(s2)+1), [False] * (len(s2)+1)
        lastdp[0] = True
        
        for i in range(1, len(s2)+1):
            lastdp[i] = lastdp[i-1] and s2[i-1] == s3[i-1]
        for i in range(1, len(s1)+1):
            curdp[0] = lastdp[0] and s1[i-1] == s3[i-1]
            for j in range(1, len(s2)+1):
                choose1, choose2 = False, False
                if s1[i-1] == s3[i+j-1] and (lastdp[j]):
                    choose1 = True
                if s2[j-1] == s3[i+j-1] and (curdp[j-1]):
                    choose2 = True
                curdp[j] = choose1 or choose2
            lastdp = curdp.copy()
        return lastdp[-1]