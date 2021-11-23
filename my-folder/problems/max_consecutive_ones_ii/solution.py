class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcnt = 0
        cnt = 0
        nextstart = 0
        meetzero = False
        for i in range(len(nums)):
            if nums[i] == 0:
                if not meetzero:
                    meetzero = True
                    nextstart = i
                else:
                    cnt = i - nextstart
                    maxcnt = max(maxcnt, cnt)
                    nextstart = i
                    continue
            
            cnt += 1
            maxcnt = max(cnt, maxcnt)
        return maxcnt