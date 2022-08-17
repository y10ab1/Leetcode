class SparseVector:
    def __init__(self, nums: List[int]):
        self.valhash = defaultdict(int)
        self.nonzerocnt = 0
        for i,n in enumerate(nums):
            if n != 0:
                self.valhash[i] = n
                self.nonzerocnt += 1
                
    def __len__(self):
        return self.nonzerocnt

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v1 = self.valhash if self.nonzerocnt <= len(vec) else vec.valhash
        v2 = self.valhash if self.nonzerocnt > len(vec) else vec.valhash
        res = 0
        for index, val in v1.items():
            res+=val*v2[index]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)