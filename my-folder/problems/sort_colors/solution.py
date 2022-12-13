class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l+=1
        l = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 2:
                nums[i], nums[l] = nums[l], nums[i]
                l-=1
                
            

