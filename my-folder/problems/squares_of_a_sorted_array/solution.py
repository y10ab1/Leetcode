class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        idx = find_cross_zero_id(nums)
        
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        
        back_nums = nums[0:idx]
        back_nums = back_nums[::-1]
        if idx < len(nums):
            nums = nums[idx:]
        else:
            nums=[]

        
        ans = []
        a=0
        b=0
        while a!=len(nums) and b!=len(back_nums):
            if nums[a] < back_nums[b]:
                ans.append(nums[a])
                a+=1
            else:
                ans.append(back_nums[b])
                b+=1
        if len(nums) - a > len(back_nums)-b:
            ans += nums[a:]
        else:
            ans += back_nums[b:]
        
        return ans
            
def find_cross_zero_id(nums):
    if nums[0] >= 0:
        return 0
    elif nums[-1] < 0:
        return len(nums)
    for i in range(len(nums)-1):
        if nums[i] < 0 and nums[i+1] >= 0:
            return i+1