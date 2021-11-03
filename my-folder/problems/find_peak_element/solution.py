class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        def p(i,r,l):
            if nums[r] > nums[i] and nums[i] > nums[l]:
                return True
            else:
                return False
        def n(i,r,l):
            if nums[r] < nums[i] and nums[i] < nums[l]:
                return True
            else:
                return False
        
        l, r = 0, len(nums)-1
        while True:
            m = (l+r)//2
            
            if m == 0 and nums[m] > nums[m+1]:
                return m
            elif m == len(nums) -1 and nums[m] > nums[m-1]:
                return m
            elif (nums[m]>nums[m-1] and nums[m]>nums[m+1]) :
                return m
            elif p(m,m+1,m-1):
                l = m+1
            elif n(m,m+1,m-1):
                r = m
            else:
                r = m
            
            