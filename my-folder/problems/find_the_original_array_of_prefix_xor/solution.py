class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return pref
        arr = [pref[0]]
        a = arr[0]
        b = arr[0]
        for i in range(1,len(pref)):
            a^=pref[i]
            arr.append(a)
            b^=arr[i]
            a=b
        return arr