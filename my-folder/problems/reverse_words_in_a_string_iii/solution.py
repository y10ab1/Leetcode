class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split(" ")
        ans = ""
        for word in slist:
            ans+=word[::-1]+" "
        return ans[:-1]