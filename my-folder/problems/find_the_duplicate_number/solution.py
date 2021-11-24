class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums[abs(i)] > 0:
                nums[abs(i)] *= -1
            else:
                return abs(i)
            