class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(arr, now):
            if not arr:
                ans.append(now)
            for i in range(len(arr)):
                dfs(arr[:i]+arr[i+1:],now+[arr[i]])
        dfs(nums,[])
        return ans