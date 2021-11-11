class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cu = [0 for _ in range(len(nums))]
        mi = nums[0]
        for i in range(len(nums)):
            cu[i] = (nums[i] + cu[i-1])
            mi = min(mi, cu[i])
        if mi > 0:
            return 1
        else:
            return 1 - mi
        