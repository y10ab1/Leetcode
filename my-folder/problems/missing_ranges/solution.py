class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [f"{lower}->{upper}"]
        res = []
        if nums[0]-lower>=2:
            res.append(f"{lower}->{nums[0]-1}")
        elif nums[0]-lower==1:
            res.append(str(lower))
            
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 2:
                res.append(str(nums[i+1]-1))
            elif nums[i+1]-nums[i] > 2:
                res.append(f"{nums[i]+1}->{nums[i+1]-1}")
        if upper-nums[-1]>=2:
            res.append(f"{nums[-1]+1}->{upper}")
        elif upper-nums[-1]==1:
            res.append(str(upper))
        return res