class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:

            if t == '+':
                tmp = s.pop()
                s[-1]+=tmp
            elif t == '-':
                tmp = s.pop()
                s[-1]-=tmp
            elif t == '*':
                tmp = s.pop()
                s[-1]*=tmp
            elif t == '/':
                tmp = s.pop()
                s[-1] = int(s[-1]/tmp)
            else:
                s.append(int(t))

        return s[-1]

                