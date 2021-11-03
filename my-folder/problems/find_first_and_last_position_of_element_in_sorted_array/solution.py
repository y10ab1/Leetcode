class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        ans = [-1,-1]
        for _ in nums:
            if nums[l] == target and ans[0] == -1:
                ans[0] = l
            else:
                l+=1
            if nums[r] == target and ans[1] == -1:
                ans[1] = r
            else:
                r-=1
        return ans
        
                