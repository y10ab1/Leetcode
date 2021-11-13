class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for i in arr:
            d[i] += 1
        tmpd = [v for (_,v) in d.items()]
        tmpd = sorted(tmpd, reverse = True)
        
        cnt = 0
        n = len(arr)
        for cnt in range(len(tmpd)):
            n -= tmpd[cnt]
            if n <= len(arr)/2:
                break
        

        return cnt+1
            