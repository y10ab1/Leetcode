class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for i in range(len(nums)-1):
            ans.append(nums[i+1]+ans[i])
        return ans