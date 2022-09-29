class MedianFinder:

    def __init__(self):
        self.smallh, self.largeh = [], []
        self.size = 0

    def addNum(self, num: int) -> None:
        if len(self.largeh) > 0 and num >= self.largeh[0]:
            heapq.heappush(self.largeh, num)
        else:
            heapq.heappush(self.smallh, -num)
        
        if len(self.largeh) > len(self.smallh):
            heapq.heappush(self.smallh, -heapq.heappop(self.largeh))
            
        elif len(self.largeh) < len(self.smallh):
            heapq.heappush(self.largeh, -heapq.heappop(self.smallh))
            
        
        self.size += 1
        

    def findMedian(self) -> float:
        if self.size%2==0:
            return (self.largeh[0]-self.smallh[0])/2
        else:
            if len(self.largeh) > len(self.smallh):
                return self.largeh[0]
            else:
                return -self.smallh[0]
            
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()