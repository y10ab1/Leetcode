class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        LtoR = [nums[0]]*len(nums)
        RtoL = [nums[-1]]*len(nums)
        for i in range(1,len(nums)):
            LtoR[i] = (LtoR[i-1]+nums[i])
            RtoL[len(nums)-i-1] = (RtoL[len(nums)-i]+nums[len(nums)-i-1])
        
        for i in range(len(nums)):
            if i == 0 and RtoL[1]==0:
                return i
            elif i == len(nums)-1 and LtoR[-2] == 0:
                return i
            elif i!= len(nums)-1 and i!=0 and LtoR[i-1] == RtoL[i+1]:
                return i
        return -1
                
                