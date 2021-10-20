class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        second = len(nums)-1
        for i in range(len(nums)):
            while nums[i]==2 and i<second:
                nums[i], nums[second] = nums[second], nums[i]
                second-=1
            while nums[i]==0 and i>zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero+=1
            if second <= zero :
                break
        