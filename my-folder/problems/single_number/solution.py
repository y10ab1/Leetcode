class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = nums[0]
        for i in range(len(nums)-1):
            ans ^= nums[i+1]
        return ans