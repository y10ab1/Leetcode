class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        nsb2 = Counter(bin(num2))['1']
        nsb1 = Counter(bin(num1))['1']
        ans = [c for c in bin(num1)[2:]]
        ans = ['0' for _ in range(31-len(ans))]+ans
        if nsb1 > nsb2:
            i = nsb1-nsb2
            for j in range(len(ans)-1,-1,-1):
                if ans[j] == '1':
                    ans[j] = '0'
                    i-=1
                if i == 0:
                    break
        elif nsb2 > nsb1:
            i = nsb2-nsb1
            for j in range(len(ans)-1,-1,-1):
                if ans[j] == '0':
                    ans[j] = '1'
                    i-=1
                if i == 0:
                    break
        return int("".join(ans),2)
            
                
        
