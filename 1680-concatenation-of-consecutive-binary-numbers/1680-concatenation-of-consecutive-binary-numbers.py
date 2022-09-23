class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ret = 1
        M = (10**9+7)
        for i in range(2,n+1):
            ret = ((ret << (len(bin(i))-2)) +i)%M
        
        return ret