class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # At least half elements in changed will be even
        n = len(changed)
        if n%2 != 0:
            return []
        ans = []
        cnt = collections.Counter(changed)
        
        keys = sorted(cnt.keys())
        
        for k in keys:
            while cnt[k]>0 and cnt[k*2]>0:
                cnt[k*2]-=1
                cnt[k]-=1
                ans.append(k)

                
        if len(ans)*2 == n and not any(cnt.values()):
            return ans
        return []
                