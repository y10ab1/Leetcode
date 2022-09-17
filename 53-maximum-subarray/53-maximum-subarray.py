class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum,cursum = -10001,-10001
        for n in nums:
            if 0 > cursum:
                cursum = n
            else:
                cursum += n
            maxsum = max(cursum, maxsum)
        return maxsum
            
            