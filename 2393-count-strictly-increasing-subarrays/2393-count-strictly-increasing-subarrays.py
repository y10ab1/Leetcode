class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        l = 0
        for r in range(1, n):
            if nums[r] > nums[r-1]:
                ans += r-l
            else:
                l,r=r,r+1
        return ans