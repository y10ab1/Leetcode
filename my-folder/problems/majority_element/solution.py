class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted([(v,k) for k,v in Counter(nums).items()])[-1][1]