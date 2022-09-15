class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        
        
        pre1, cur1 = nums[0], max(nums[1], nums[0])
        pre2, cur2 = nums[1], max(nums[1], nums[2])
        
        
        for i in range(2,n-1):
            pre1, cur1 = cur1, max(pre1+nums[i],cur1)
            pre2, cur2 = cur2, max(pre2+nums[i+1],cur2)
            
        
        
            
        
        return max(cur1,cur2)
            