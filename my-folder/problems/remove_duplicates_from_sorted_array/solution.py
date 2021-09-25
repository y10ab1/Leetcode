class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        last = -1000
        for i in range(len(nums)):
            if last != nums[i]:
                nums[c] = nums[i]
                last = nums[i]
                c+=1
        
        return c