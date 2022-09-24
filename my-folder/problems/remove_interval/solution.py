class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        def overlap(A: List[int], B: List[int]) -> List[int]:
            # all out
            if A[1] <= B[0] or A[0] >= B[1]:
                return A
            # right in
            if A[1] > B[0] >A[0]:
                return [A[0],B[0]]
            # all in
            if A[0] >= B[0] and A[1] <= B[1]:
                return []
            # left in
            if A[0] < B[1] < A[1]:
                return [B[1], A[1]]
            
        ret = []
        intervals
        for interval in intervals:
            if interval[0] < toBeRemoved[0] and interval[1] > toBeRemoved[1]:
                ret += [[interval[0],toBeRemoved[0]],[toBeRemoved[1],interval[1]]]
                continue
            l = overlap(interval, toBeRemoved)
            if l:
                ret.append(l)
        
        return ret