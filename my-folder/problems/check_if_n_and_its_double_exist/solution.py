class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        exist2 = {}
        zero = 0
        for i in arr:
            exist2[i] = True
            if i == 0:
                zero+=1
        if zero >1:
            return True
        
        for idx,i in enumerate(arr):
            try:
                if i != 0:
                    return exist2[i*2]
            except:
                pass
        return False