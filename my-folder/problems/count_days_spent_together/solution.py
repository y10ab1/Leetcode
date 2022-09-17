class Solution:
    def countDaysTogether(self, aa: str, la: str, ab: str, lb: str) -> int:
        month_days = {i:d for i,d in enumerate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])}
        acc = [0]*13

        for i in range(len(month_days)):
            acc[i] = month_days[i]+acc[i-1]
        
        
        aa = (int(aa.split("-")[0]), int(aa.split("-")[1]))
        la = (int(la.split("-")[0]), int(la.split("-")[1]))
        
        ab = (int(ab.split("-")[0]), int(ab.split("-")[1]))
        
        lb = (int(lb.split("-")[0]), int(lb.split("-")[1]))
        
        if aa>lb or ab>la:
            return 0
        
        start = max(aa,ab)
        end = min(la,lb)
        start = start[1]+acc[start[0]-2]
        end = end[1]+acc[end[0]-2]      
        return end-start+1