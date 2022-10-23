class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for k,v in Counter(nums).items():
            if v>1:
                return [k,(set(range(1,len(nums)+1)) - set(nums)).pop()]