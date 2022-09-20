class Solution:
    def maxProduct(self, pre: List[int]) -> int:
        suf =  pre[::-1]
        for i in range(1,len(pre)):
            pre[i] *= pre[i-1] or 1
            suf[i] *= suf[i-1] or 1    
        return max(pre+suf)