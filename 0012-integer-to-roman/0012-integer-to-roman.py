class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1:'I'
            ,4:'IV'
            ,5:'V'
            ,9:'IX'
            ,10:'X'
            ,40:'XL'
            ,50:'L'
            ,90:'XC'
            ,100:'C'
            ,400:'CD'
            ,500:'D'
            ,900:'CM'
            ,1000:'M'}
        ans = []
        dig = 1
        while num>0:
            n = int(num%10)
            if n<4:
                for i in range(n):
                    ans.append(d[dig])
            elif 6<=n<9:
                for i in range(5,n):
                    ans.append(d[dig])
                ans.append(d[5*dig])
            else:
                ans.append(d[n*dig])
            num/=10
            dig*=10
        return "".join(ans[::-1])
            