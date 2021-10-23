class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start, cnt = 0, 0
        for i, c in enumerate(s):
            if c in d and start<=d[c]:
                start = d[c] +1
            else:
                
                cnt = max(cnt, i-start+1)
            d[c] = i
                
                
        return cnt