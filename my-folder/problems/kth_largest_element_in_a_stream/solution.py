class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums 
        self.k = k
        heapq.heapify(self.h)
        for _ in range(len(nums)-k):
            heapq.heappop(self.h)
        

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heappush(self.h, val)
            heapq.heappop(self.h)
        
        return self.h[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)