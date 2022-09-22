class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split(" ")
        ans = ""
        for word in slist:
            for i in range(len(word)-1,-1,-1):
                ans+=word[i]
            ans+=" "
        return ans[:-1]