class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        leftspace = [i-j for i,j in zip(capacity, rocks) ]
        leftspace.sort()
        ans = 0
        while additionalRocks > 0 and ans < len(leftspace):
            minval = leftspace[ans]
            if additionalRocks >= minval:
                ans +=1
            additionalRocks -= minval
        return ans