class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-3,-1,-1):
            a,b,c = nums[i:i+3]
            if (a+b>c) and (a+c>b) and (b+c>a):
                return a+b+c
        return 0