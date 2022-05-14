class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        calsum = 0
        calnums = []
        ans = 0
        for n in nums:
            calsum += n
            calnums.append(calsum)
        
        for i in range(len(nums)-1):
            if calnums[i] >= calnums[-1] - calnums[i]:
                ans +=1
        return ans