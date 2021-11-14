class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = [1,1,1,1,1]
        for i in range(n-1):
            t = a.copy()
            for j in range(5):
                o = 0
                for k in range(j+1):
                    o+=t[k]
                a[j] = o
        return sum(a)