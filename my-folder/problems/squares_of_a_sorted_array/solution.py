class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        p, n = [], []
        for i in range(len(nums)):
            if nums[i] >= 0:
                p = nums[i:]
                n = nums[:i]
                break
        if len(p) == 0 and len(n) == 0:
            n = nums
        n = n[::-1]
        
        for i in range(len(p)):
            p[i] = p[i]**2
        for i in range(len(n)):
            n[i] = n[i]**2
        idp, idn = 0, 0
        while idp < len(p) and idn < len(n):
            if p[idp] < n[idn]:
                ans.append(p[idp])
                idp+=1
            else:
                ans.append(n[idn])
                idn+=1
        
        if idp >= len(p):
            ans+=n[idn:]
        else:
            ans+=p[idp:]
        return ans