class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        cnt=0
        for i,x in enumerate(sorted(heights)):
            if x != heights[i]:
                cnt+=1
        return cnt
        