class Solution:
    def removeDuplicates(self, s: str) -> str:
        t = ['0']
        for c in s:
            if t[-1] == c:
                t.pop()
            else:
                t.append(c)
        return "".join(t[1:])