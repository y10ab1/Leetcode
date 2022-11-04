class Solution:
    def reverseVowels(self, s: str) -> str:
        q = []
        se = set(['a','e','i','o','u','A','E','I','O','U'])
        s = [c for c in s]
        
        for w in s:
            if w in se:
                q.append(w)
                
        q = deque(q[::-1])
        
        for i in range(len(s)):
            if s[i] in se:
                s[i] = q.popleft()
                
        return "".join(s)