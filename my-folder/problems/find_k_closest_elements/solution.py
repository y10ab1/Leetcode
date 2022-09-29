class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        for a in arr:
            heapq.heappush(h,(abs(x-a),a))
        return sorted([heapq.heappop(h)[1] for i in range(k)])