class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                print(d[target - n ])
                return [d[target - n ], i]
            else:
                d[n] = i