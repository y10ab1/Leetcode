class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l<r:
            m = (l+r)//2
            if target > nums[0] and nums[m] >= nums[0]:
                if nums[m] > target:
                    r = m
                elif nums[m] < target:
                    l = m+1
                else:
                    return m
            elif target < nums[0] and nums[m] < nums[0]:
                if nums[m] > target:
                    r = m
                elif nums[m] < target:
                    l = m+1
                else:
                    return m
            elif target > nums[0] and nums[m] < nums[0]:
                r = m
            elif target < nums[0] and nums[m] >= nums[0]:
                l = m+1
            elif target == nums[0]:
                return 0
        if nums[l] == target:
            return l
        return -1
            
            