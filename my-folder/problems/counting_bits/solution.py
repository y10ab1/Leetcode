class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0,1,1]
        for i in range(3,n+1):
            if i%2 == 0:
                ans.append(ans[i//2])
            else:
                ans.append(ans[i-1]+1)
        return ans[:n+1]