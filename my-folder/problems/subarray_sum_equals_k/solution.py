class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = {}
        presum[0] = 1
        ans = 0
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if (Sum-k) in presum:
                ans += presum[Sum-k]
            if Sum in presum:
                presum[Sum]+=1
            else:
                presum[Sum]=1
            
        return ans
            