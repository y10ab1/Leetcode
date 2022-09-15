class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        ans = 0
        keys = sorted(d.keys())
        pre,cur = 0, d[keys[0]]*keys[0]
        for i in range(1,len(keys)):
            k = keys[i]
            if k-1 == keys[i-1]:
                pre, cur = cur, max(cur, d[k]*k+pre)
            else:
                pre, cur = cur, cur+d[k]*k
            
            
        return cur