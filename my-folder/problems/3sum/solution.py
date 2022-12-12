class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        
        nums = []
        for k,v in d.items():
            if v >= 3:
                nums += [k for _ in range(3)]
            else:
                nums += [k for _ in range(v)]
        ans = set()
        for i in range(len(nums)-1):
            s = {}
            for j in range(i+1,len(nums)):
                if nums[j] in s:
                    ans.add(tuple(sorted(s[nums[j]]+[nums[j]])))
                else:
                    s[-(nums[i]+nums[j])] = [nums[i],nums[j]]

        return list(ans)
