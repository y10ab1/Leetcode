class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_cnt = 0
        for i in s:
            if i-1 not in s:
                cur = i
                cur_cnt = 1
                
                while cur + 1 in s:
                    cur += 1
                    cur_cnt += 1
                max_cnt = max(max_cnt, cur_cnt)
        return max_cnt
                
            