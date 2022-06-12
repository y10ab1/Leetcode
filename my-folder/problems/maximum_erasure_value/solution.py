class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, r, S, cursum, ans = 0, 0, dict(), 0, 0
        
        while r < len(nums):
            if nums[r] not in S:
                S[nums[r]] = None
                cursum += nums[r]
                r += 1
                ans = max(cursum, ans)
            else:
                del S[nums[l]]
                cursum -= nums[l]
                l += 1

        return ans