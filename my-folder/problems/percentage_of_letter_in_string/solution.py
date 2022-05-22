class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
            
        return int((100 * d[letter]/len(s)))