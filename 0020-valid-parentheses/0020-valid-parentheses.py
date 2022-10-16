class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif stack:
                if c != d[stack.pop()]:
                    return False
            else:
                return False
        if stack:
            return False
        return True