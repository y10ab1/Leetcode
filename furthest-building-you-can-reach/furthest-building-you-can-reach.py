class Solution:
    def furthestBuilding(self, h: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(len(h)-1):
            d = h[i+1]-h[i]
            if d > 0:
                heapq.heappush(pq,d)
            if len(pq) > ladders:
                bricks-=heapq.heappop(pq)
            if bricks<0:
                return i
        return len(h)-1