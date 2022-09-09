class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        p.sort(key=lambda x: (-x[0],x[1]))
        cnt = 0
        curmax = 0
        for _, d in p:
            if d < curmax:
                cnt +=1
            else:
                curmax = d
        return cnt
            