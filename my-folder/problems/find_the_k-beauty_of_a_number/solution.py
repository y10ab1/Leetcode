class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numstr = str(num)
        ans = 0
        for i in range(len(numstr)-k+1):
            div = int(numstr[i:i+k])
            if div != 0 and num % div == 0:
                ans += 1
        return ans