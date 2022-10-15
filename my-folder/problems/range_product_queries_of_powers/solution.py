class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        m = 10**9+7
        p = []
        ans = []
        i = 31
        while i >= 0:
            if n<=0:
                break
            if 2**i <= n:
                n-=2**i
                p.append(2**i)
            else:
                i-=1
        p=p[::-1]
        print(p,n)
        
        for l,r in queries:
            base = 1
            for pp in p[l:r+1]:
                base*=(pp)
            ans.append(base%m)
        return ans
        
            