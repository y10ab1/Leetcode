class Solution:
    def kWeakestRows(self, board: List[List[int]], k:int) -> List[int]:
        s = [(sum(row),idx) for idx, row in enumerate(board)]
        s.sort()
        ans = [idx for _,idx in s]
        return ans[:k]