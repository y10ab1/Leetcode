class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        maxid, max2id = 0, 1
        max2num = nums[1]
        maxnum = nums[0]
        for i in range(len(nums)):
            if nums[i] > maxnum:
                max2id = maxid
                maxid = i
                maxnum, max2num = nums[maxid], nums[max2id]
            elif nums[i] > max2num and i != maxid:
                max2id = i
                max2num = nums[i]
        if nums[maxid] >= nums[max2id]*2:
            return maxid
        else:
            return -1