class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for t in tokens:
            ans = 0
            if t == '+':
                b = numStack.pop()
                a = numStack.pop()
                ans = a+b
                print(ans)
                numStack.append(ans)
            elif t == '-':
                b = numStack.pop()
                a = numStack.pop()
                ans = a-b
                print(ans)
                numStack.append(ans)
            elif t == '*':
                b = numStack.pop()
                a = numStack.pop()
                ans = a*b
                print(ans)
                numStack.append(ans)
            elif t == '/':
                b = numStack.pop()
                a = numStack.pop()
                ans = a/b
                if ans < 0:
                    ans = -1*(-1*ans //1)
                else:
                    ans = ans // 1
                
                numStack.append(ans)
            else:
                numStack.append(int(t))
            
        return int(numStack.pop())
            