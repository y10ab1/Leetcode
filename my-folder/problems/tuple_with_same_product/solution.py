class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n,ans = len(nums),0
        for i in range(n):
            for j in range(i+1,n):
                k = nums[i]*nums[j]
                ans+=d[k]
                d[k]+=1
        
        
        return 8*ans
