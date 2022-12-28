class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)
        for _ in range(k):
            num = heapq.heappop(piles)
            
            heapq.heappush(piles, num//2)
        
        return -sum(piles)