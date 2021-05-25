class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum = {}
        presum[0] = -1
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if not (Sum%k in presum):
                    presum[Sum%k] = i 
            
            if i - presum[Sum%k] >= 2:
                return True
            
                
        return False
