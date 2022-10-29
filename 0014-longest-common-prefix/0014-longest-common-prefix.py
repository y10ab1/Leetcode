class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(201):
            for j in range(len(strs)):
                if len(strs[j])-1 < i or len(strs[j-1])-1 < i or strs[j][i] !=strs[j-1][i]:
                    return strs[j-1][:i]
