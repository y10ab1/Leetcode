class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        maxval = logs[0][1]
        rid = logs[0][0]
        for i in range(1,len(logs)):
            u = logs[i][1]-logs[i-1][1]
            if u > maxval:
                maxval = u
                
                rid = logs[i][0]
            elif u == maxval and logs[i][0] < rid:
                rid = logs[i][0]
        return rid
            