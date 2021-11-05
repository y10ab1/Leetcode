class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        pos = (dividend > 0) == (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        while (dividend - divisor) >= 0:
            temp, i = divisor, 1
            while dividend >= temp:
                ans += i
                dividend -= temp
                i<<=1
                temp<<=1
        if pos:
            return max(min(ans,2147483647),-2147483648)
        else:
            return max(min(-ans,2147483647),-2147483648)