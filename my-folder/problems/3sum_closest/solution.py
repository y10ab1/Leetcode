class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s == target:
                    return s
                if abs(s-target) < abs(res-target):
                    res = s
                    
                if s > target:
                    r-=1
                else:
                    l+=1

        return res
            