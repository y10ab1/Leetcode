class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        ans = 0
        cur = 0
        for i in nums:
            if i == m:
                cur+=1
                ans = max(cur,ans)
            else:
                cur = 0
        return ans