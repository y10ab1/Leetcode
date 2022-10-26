class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # sum(nums[:j]) % k == sum(nums[:i]) % k
        d = {0:-1}
        acc = 0
        for i,n in enumerate(nums):

            acc+=n
            if acc%k not in d:
                d[acc%k] = i
            elif i - d[acc%k]>1:
                return True

        return False