class Solution:
    def concatenatedBinary(self, n: int) -> int:
        length,ret = 0,0
        M = (10**9+7)
        for i in range(1,n+1):
            if i&(i-1) ==0:
                length+=1
            ret=(i+(ret<<length))%M
        
        return ret