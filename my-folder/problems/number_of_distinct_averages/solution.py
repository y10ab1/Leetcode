class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        nums.sort()
        s = set()
        while l<r:
            s.add(nums[l]+nums[r])
            l+=1
            r-=1
        return len(s)