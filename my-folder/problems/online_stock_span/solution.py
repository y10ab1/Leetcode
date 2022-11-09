class StockSpanner:

    def __init__(self):
        self.s = [(10001,1)]

    def next(self, price: int) -> int:
        cnt = 1
        while self.s[-1][0] <= price:
            cnt+=self.s.pop()[1]
        self.s.append((price,cnt))
        return cnt

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)