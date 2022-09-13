class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # start with 0         than OK
        # start with 110       than still need 1 10
        # start with 1110      than still need 2 10
        # start with 11110     than still need 3 10
        bstr = [f'{s:08b}' for s in data]
        i = 0
        while i < len(bstr):
            b = bstr[i]
            if b[0] == '0':
                i+=1
            elif b[:3] == '110':
                for j in range(1,2):
                    if i+j>=len(bstr) or bstr[i+j][:2] != '10':
                        return False
                i+=2
            elif b[:4] == '1110':
                for j in range(1,3):
                    if i+j>=len(bstr) or bstr[i+j][:2] != '10':
                        return False
                i+=3
            elif b[:5] == '11110':
                for j in range(1,4):
                    if i+j>=len(bstr) or bstr[i+j][:2] != '10':
                        return False
                i+=4
            else:
                return False
            
        return True