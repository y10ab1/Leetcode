class Solution:
    def latestTimeCatchTheBus(self, b: List[int], p: List[int], capacity: int) -> int:
        p.sort()
        b.sort()
        onboard_cnt = 0
        for bus in b:
            cap = capacity
            while cap>0 and onboard_cnt<len(p) and p[onboard_cnt] <=bus :
                cap-=1
                onboard_cnt+=1
        
        
        lasttime = b[-1] if cap>0 else p[onboard_cnt-1]
        
        while lasttime in set(p):
            lasttime-=1
        return lasttime
