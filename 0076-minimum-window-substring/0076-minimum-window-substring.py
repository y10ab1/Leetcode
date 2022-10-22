class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = ""
        maxlen = float('inf')
        l,r = 0,0
        td = Counter(t)
        sd = Counter(s[0])
        while True:
            
            valid = True
            for n in td:
                if td[n] > sd[n]:
                    valid = False
                    break
                    
            if valid:
                if len(s[l:r+1]) < maxlen:
                    maxlen = len(s[l:r+1])
                    ret = s[l:r+1]
                sd[s[l]]-=1
                l+=1
                continue
                
            r+=1
            if r<len(s):
                sd[s[r]]+=1
            else:
                break

        return ret
        