class Solution:
    def numSplits(self, s: str) -> int:
        p, q = {}, {}
        ans = 0
        p[s[0]] = 1
        for i in range(1,len(s)):
            if q.get(s[i]):
                q[s[i]] += 1
            else:
                q[s[i]] = 1
        if len(p) == len(q):
            ans += 1
        for i in range(1,len(s)-1):
            if p.get(s[i]):
                p[s[i]] += 1
            else:
                p[s[i]] = 1
            if q[s[i]] > 1:
                q[s[i]] -= 1
            elif q[s[i]] == 1:
                q.pop(s[i], None)
            if len(p) == len(q):
                ans += 1
        return ans
            