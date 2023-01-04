class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s,[],res)
        return res
    def dfs(self, s: str, path: list, res: list) -> None:
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPali(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
    def isPali(self, s: str) -> bool:
        return s == s[::-1]