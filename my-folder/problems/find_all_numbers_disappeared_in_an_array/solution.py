class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        snum = set(nums)
        sans = set(range(1,len(nums)+1))
        a = sans - snum
        
        return list(a)
        