class MyCalendarThree:

    
    # overlap :
    # prestart <= start < preend
    # prestart < end < preend 
    def __init__(self):
        self.events = defaultdict(int)


    def book(self, start: int, end: int) -> int:
        self.events[start]+=1
        self.events[end]-=1
        maxcnt,cnt = 0,0
        for k in sorted(self.events.keys()):
            cnt+=self.events[k]
            
            maxcnt = max(cnt,maxcnt)
            
        return maxcnt
    

        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)