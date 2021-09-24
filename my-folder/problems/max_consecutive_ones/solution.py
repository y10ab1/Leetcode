class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Max_cnt = 0
        cur_cnt = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                cur_cnt = 0
            elif nums[i] == 1:
                cur_cnt += 1
                if Max_cnt < cur_cnt:
                    Max_cnt = cur_cnt
        return Max_cnt