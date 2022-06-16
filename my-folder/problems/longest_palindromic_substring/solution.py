class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(self.longestSubstring(s,i,i), self.longestSubstring(s,i,i+1), res, key=len)
        return res
            
    def longestSubstring(self, s: str, l: int, r: int) -> str:
        longestStr = ""
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l, r = l-1, r+1
            else:
                break
        return s[l+1: r]
