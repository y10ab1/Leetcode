class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        h = [(0,0)]
        for i in range(1,len(nums)):
            while h:
                jump, idx = heapq.heappop(h)
                if i - idx <= nums[idx]:
                    heapq.heappush(h, (jump+1,i))
                    heapq.heappush(h, (jump,idx))
                    ans = jump+1
                    break
        return ans
                    