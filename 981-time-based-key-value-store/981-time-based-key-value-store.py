class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.d[key],(timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_left(self.d[key],(timestamp+1,""))
        if len(self.d[key]) and i>0:
            return self.d[key][i-1][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)