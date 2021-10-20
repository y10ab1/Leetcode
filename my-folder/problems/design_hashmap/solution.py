class MyHashMap:

    def __init__(self):
        self.mymap = [None]*1000001

    def put(self, key: int, value: int) -> None:
        self.mymap[key] = value

    def get(self, key: int) -> int:
        if self.mymap[key] == None:
            return -1
        else:
            return self.mymap[key]
        
    def remove(self, key: int) -> None:
        self.mymap[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)