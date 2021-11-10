class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class DSet:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [1] * size
                
            def find(self, x):
                if x == self.root[x]:
                    return x
                else:
                    self.root[x] = self.find(self.root[x])
                    return self.root[x]
                
            def union(self, x, y):
                X = self.find(x)
                Y = self.find(y)
                if self.rank[X] > self.rank[Y]:
                    self.root[Y] = self.root[X]
                elif self.rank[X] < self.rank[Y]:
                    self.root[X] = self.root[Y]
                else:
                    self.root[Y] = self.find(X)
                    self.rank[X] += 1
                    
        DS = DSet(len(s))
        ans = ''
        m = defaultdict(list)
        for p in pairs:
            DS.union(p[0],p[1])
        for i in range(len(s)):
            m[DS.find(i)].append(s[i])
        for i in m:
            m[i].sort(reverse = True)
        for i in range(len(s)):
            ans += (m[DS.find(i)].pop())
        return ans
        
            