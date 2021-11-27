class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in words1:
            d1[i] += 1
        for j in words2:
            d2[j] += 1
        ans = 0
        for i in d1:
            if d1[i] == 1 and d2[i] == 1:
                ans += 1
        return ans