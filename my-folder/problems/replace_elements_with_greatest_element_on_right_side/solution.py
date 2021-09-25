class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        Max_arr = [0]*len(arr)
        maxnum = -1
        i = len(arr)-1
        while i >=0:
            Max_arr[i] = maxnum
            if arr[i] > maxnum:
                maxnum = arr[i]
            i-=1
        return Max_arr