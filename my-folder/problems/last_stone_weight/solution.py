class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapify(stones)
        
        while len(stones) > 1:
            
            a = heappop(stones)*-1
            b = heappop(stones)*-1
            if a-b:
                heappush(stones, (a-b)*-1)
            
        if len(stones) == 1:
            return stones[0]*-1
        elif len(stones) == 0:
            return 0