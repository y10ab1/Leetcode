class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            l = len(ans)
            for r in range(l):
                ans.append(ans[r]+[i])
        return ans