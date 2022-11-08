class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for c in s:
            if st and st[-1].islower() and st[-1].upper() == c:
                st.pop()
            elif st and st[-1].isupper() and st[-1].lower() == c:
                st.pop()
            else:
                st.append(c)
        return "".join(st)