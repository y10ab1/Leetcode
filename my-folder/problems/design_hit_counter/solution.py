class HitCounter:

    def __init__(self):
        self.hit_cnt = [0]
        self.time = [float("-inf")]
    def hit(self, timestamp: int) -> None:
        self.time.append(timestamp)
        self.hit_cnt.append((self.hit_cnt[-1]+1))

    def getHits(self, timestamp: int) -> int:
        left_id = bisect_right(self.time, timestamp-300)
        return self.hit_cnt[-1] - self.hit_cnt[left_id-1]


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)