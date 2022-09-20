class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for n in nums:
            totalSum += n
            curMax = max(curMax+n,n)
            curMin = min(curMin+n,n)
            maxSum = max(curMax,maxSum)
            minSum = min(curMin,minSum)
        
        return max(maxSum, totalSum-minSum) if maxSum>0 else maxSum
            
            
                    
                
            
            