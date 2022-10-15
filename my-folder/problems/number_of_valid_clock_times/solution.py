class Solution:
    def countTime(self, time: str) -> int:
        # 0 0~9 0~5 0~9
        # 1 0~9 ..
        # 2 0~3
        
        a,b,_,c,d = time
        base = 1
        if d == '?':
            base *= 10
        if c == '?':
            base *= 6
        if a=='?' and b == '?':
            base *= 24
        elif (a=='0' or a=='1') and b == '?':
            base *= 10
        elif a=='2' and b == '?':
            base*=4
        elif a=='?' and int(b) < 4:
            base*=3
        elif a=='?' and int(b) >=4:
            base*=2
        return base
            