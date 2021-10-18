class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = {}
        for i in nums:
            c[i] = 0
        for i in nums:
            c[i]+=1
        for idx, i in enumerate(c):
            if idx>0:
                if Max < c[i]:
                    Max = c[i]
                    Maxid = i
            else:
                Max = c[i]
                Maxid = i
        return Maxid