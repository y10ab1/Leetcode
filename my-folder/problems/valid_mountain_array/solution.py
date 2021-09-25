class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        reverse = 0
        if len(arr) <3:
            return False
        if not (arr[0]<arr[1] and arr[-1]<arr[-2]):
            return False
        
        for i in range(1,len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
            if reverse == 0:
                if arr[i]>arr[i+1]:
                    reverse = 1
            elif reverse == 1:
                if arr[i]<arr[i+1]:
                    return False
            else:
                return False
        return True
            
                
                
        