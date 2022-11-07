class Solution:
    def maximum69Number (self, num: int) -> int:
        # Change left most 6 into 9
        i = 1000
        while i > 0:
            if (num//i)%10 == 6:
                num += 3*i
                return int(num)
            i/=10
        return int(num)