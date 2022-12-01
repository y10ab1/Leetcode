class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a,b=0,0
        for c,d in zip(s[:len(s)//2],s[len(s)//2:]):
            if c in v: a+=1
            if d in v: b+=1
        return a==b