class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.string = characters
        self.cmblen = combinationLength
        self.d = defaultdict(list)
        self.nextc = defaultdict(str)
        for cnt, s in enumerate(self.string):
            self.d[1].append(s)
            if cnt+1 < len(self.string):
                self.nextc[s] = self.string[cnt+1]
        for i in range(2, self.cmblen+1):
            for c in self.d[i-1]:
                startc = c[-1]
                while self.nextc[startc]:
                    self.d[i].append(c+self.nextc[startc])
                    startc = self.nextc[startc]
            self.d.pop(i-2, None)
                
            
        self.d[self.cmblen] = self.d[self.cmblen][::-1]

    def next(self) -> str:
        if self.d[self.cmblen]:
            return self.d[self.cmblen].pop()
        

    def hasNext(self) -> bool:
        if self.d[self.cmblen]:
            return True
        else:
            return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()