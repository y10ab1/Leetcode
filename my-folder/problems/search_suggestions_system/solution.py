class Solution:
    def suggestedProducts(self, A: List[str], word: str) -> List[List[str]]:
        A.sort()
        prefix = ""
        res = []
        for w in word:
            prefix += w
            i = bisect_left(A,prefix)
            res.append([B for B in A[i:i+3] if B[:len(prefix)]==prefix])
        return res
        