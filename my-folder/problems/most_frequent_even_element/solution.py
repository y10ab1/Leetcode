class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = Counter(nums)
        l = []
        for k,v in d.items():
            if k%2==0:
                l.append((-v,k))
        l.sort()
        if l:
            return l[0][1]
        else:
            return -1