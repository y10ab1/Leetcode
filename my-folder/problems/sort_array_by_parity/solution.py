class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        earr=[]
        oarr=[]
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                earr.append(nums[i])
            else:
                oarr.append(nums[i])
        earr = earr + oarr
                
        return earr
        