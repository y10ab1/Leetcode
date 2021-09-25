class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = set(nums)
        ans = []
        for x in num:
            ans.append(x)
        ans.sort()
        
        if len(ans) >= 3:
            return ans[-3]
        else:
            return ans[-1]
            
        