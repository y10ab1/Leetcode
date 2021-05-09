class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1 and target[0]!=1:
            return False
        elif len(target) == 1:
            return True
        
        target.sort()
        while(True):
            print(target)
            MaxNum = target[-1]
            Sum = sum(target)
            
            R = MaxNum % (Sum - MaxNum)
            Q = MaxNum // (Sum - MaxNum)
            if MaxNum == 1:
                return True
            elif MaxNum - (Sum - MaxNum) <=0 or (R == 0 and ((Sum - MaxNum)!=1)):
                return False
            else:
                if R == 0:
                    target[-1] = R +1
                else:
                    target[-1] = R
                for i in range(len(target)):
                    if target[-1] >= target[i-1] and target[-1] < target[i]:
                        target.insert(i,target[-1])
                        target.pop()
                        break