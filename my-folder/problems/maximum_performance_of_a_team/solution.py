class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ans = 0
        sSum = 0
        h = []
        for e,s in sorted(zip(efficiency, speed), reverse=True):
            sSum += s
            heapq.heappush(h,s)
            if len(h) >k:
                sSum-=heapq.heappop(h)
            ans = max(ans, sSum*e)
        
        
        
        return ans%(10**9+7)