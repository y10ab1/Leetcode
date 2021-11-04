class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        N = len(columnTitle)
        for i in range(N)[::-1]:
            ans += (26**(N-i-1))*(ord(columnTitle[i]) - ord('A') + 1)
        return ans