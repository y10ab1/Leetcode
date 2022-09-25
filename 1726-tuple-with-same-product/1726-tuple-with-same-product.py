class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = {}
        n,ans = len(nums),0
        for i in range(n):
            for j in range(i+1,n):
                k = nums[i]*nums[j]
                ans+=d.get(k,0)
                d[k]=1+d.get(k,0)
        
        
        return 8*ans
