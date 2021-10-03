class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        Max = nums[0]
        for i in range(1,len(nums)):
            if m >= 0:
                m += nums[i]
            else:
                m = nums[i]
            Max = max(m,Max)
        return Max
                