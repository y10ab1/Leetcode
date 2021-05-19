class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        mid = 0
        ans = 0
        if len(sort_nums)%2 == 1:
            mid = sort_nums[int(len(sort_nums)//2)]
            
            for i in sort_nums:
                if i < mid:
                    ans += (mid - i)
                else:
                    ans += (i - mid)
        else:
            mid = (sort_nums[int(len(sort_nums)//2)] + sort_nums[int(len(sort_nums)//2)-1])//2
            for i in sort_nums:
                if i < mid:
                    ans += (mid - i)
                else:
                    ans += (i - mid)
                    
        return ans
            