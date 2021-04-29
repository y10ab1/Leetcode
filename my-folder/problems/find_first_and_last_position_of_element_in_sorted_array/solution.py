class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == target:
                if cnt == 0:
                    start = i
                    end = i
                elif cnt > 0:
                    end = i
                cnt+=1
        return [start, end]