class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex + 1
        if n == 1:
            return [1]
        elif n == 2:
            return [1,1]
        else:
            ans = [1,1]
            for i in range(n-2):
                temp = ans.copy()
                for j in range(len(ans)-1):
                    ans[j+1] = temp[j]+temp[j+1]
                ans.append(1)
        return ans