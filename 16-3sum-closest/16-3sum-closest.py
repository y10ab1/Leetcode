class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if abs(s-target) < abs(res-target):
                    res = s
                if s > target:
                    r-=1
                elif s < target:
                    l+=1
                else:
                    return res
        return res
            