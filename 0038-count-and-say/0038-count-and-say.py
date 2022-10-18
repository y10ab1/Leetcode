class Solution:
    def countAndSay(self, n: int) -> str:
        pre,cur = "1","11"
        if n == 1:
            return pre
        elif n == 2:
            return cur
        
        for i in range(3,n+1):
            pre = cur
            c = "a"
            cnt = 0
            tmp = []
            for j in range(len(pre)):
                if pre[j] == c:
                    cnt+=1
                elif c=='a':
                    c,cnt = pre[j],1
                else:
                    tmp.append(f"{cnt}{c}")
                    c,cnt = pre[j],1
            tmp.append(f"{cnt}{pre[j]}")        
            cur = "".join(tmp)
        return cur