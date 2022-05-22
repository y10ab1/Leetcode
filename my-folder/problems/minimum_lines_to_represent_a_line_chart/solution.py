class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1:
            return 0
        stockPrices.sort()
        i1, j1 = stockPrices[0]
        i2, j2 = stockPrices[1]
        g = gcd((j2-j1),(i2-i1))
        prey = ((j2-j1)/g)
        prex = ((i2-i1)/g)
        ans = 1
        if len(stockPrices) == 2:
            return ans
        
        for idx in range(2, len(stockPrices)):
            i1, j1 = stockPrices[idx-1]
            i2, j2 = stockPrices[idx]        
            g = gcd((j2-j1),(i2-i1))
            y = ((j2-j1)/g)
            x = ((i2-i1)/g)
            print(prex, x, prey, y)

            if x != prex or y != prey:
                ans += 1
                prex,prey = x,y
        return ans
            
        