class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for i in nums:
            if c.get(i):
                c[i]+=1
            else:
                c[i] = 1
        f = {}
        for i in range(1,len(nums)+1):
            f[i] = []
        for i in c:
            f[c[i]].append(i)
        ans = []
        for i in f:
            ans += f[i]
        return ans[len(ans)-k:]
                
            