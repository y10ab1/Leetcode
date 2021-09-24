class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        OK = 0
        c = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[c] = nums[i]
                OK+=1
                c+=1
        return OK
                