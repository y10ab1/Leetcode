class LUPrefix:

    def __init__(self, n: int):
        self.check = defaultdict(int)
        self.check[0] = 2
        self.LU = 0
        # 0,1,2= no up finish

    def upload(self, video: int) -> None:
        if self.check[video-1] == 2:
            self.check[video] = 2
        else:
            self.check[video] = 1
        
        while self.check[self.LU+1] >= 1:
            self.check[self.LU+1] = 2
            self.LU+=1
            

    def longest(self) -> int:
        return self.LU
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()