class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        s = Counter(words)
        for k in s:
            if k[0]!=k[1] and k[::-1] in s:
                res+= min(s[k],s[k[::-1]])*2
            elif k[0]==k[1] and s[k]>1:
                res += s[k]*2 if s[k]%2==0 else (s[k]-1)*2
        res += 2 if any([k[0]==k[1] for k in s if s[k]%2==1]) else 0
        return res
        