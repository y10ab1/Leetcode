class Solution:
    def reverseWords(self, s: str) -> str:
        print(s.split(' ')[::-1])
        return " ".join([c for c in s.split(' ')[::-1] if c!=''])