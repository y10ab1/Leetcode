# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def BS(low,high):
            mid = (low+high)//2
            
            r = guess(mid)
            print(mid,r)
            if r == 0:return mid
            elif r == 1:return BS(mid+1,high)
            else :return BS(0,mid-1)
        return BS(0,n)