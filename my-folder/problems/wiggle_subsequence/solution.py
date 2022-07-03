class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 0:
                inc = dec + 1
            elif diff < 0:
                dec = inc + 1
        return max(dec, inc)