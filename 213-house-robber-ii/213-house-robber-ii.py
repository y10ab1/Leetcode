class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        
        
        pre, cur = nums[0], max(nums[1], nums[0])
        
        for i in range(2,n-1):
            pre, cur = cur, max(pre+nums[i],cur)
        s0 = cur
        
        pre, cur = nums[1], max(nums[1], nums[2])
        
        for i in range(3,n):
            pre, cur = cur, max(pre+nums[i],cur)
            
        s1 = cur
        
        return max(s1,s0)
            