class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum,cursum = -10001,-10001
        for n in nums:
            if cursum>=0:
                cursum += n
            else:
                cursum = n
            maxsum = max(cursum, maxsum)
        return maxsum
            
            