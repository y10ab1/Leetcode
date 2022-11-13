class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([c for c in s.split(' ')[::-1] if c!=''])