class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        ans = len(nums)
        l = 0
        for r in range(1, len(nums)):
            if nums[r] > nums[r-1]:
                ans += r-l
            else:
                l,r=r,r+1
        return ans