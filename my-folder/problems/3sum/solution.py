class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <3:
            return []
        nums = sorted(nums)
        print(nums)
        d = {}
        
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans = []
        for i in range(len(nums)-2):
            j = i+1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while j < len(nums):
                if i!=j-1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                s = 0 - nums[i] - nums[j]
                if s in d and s>=nums[j] and nums[j]>=nums[i]:
                    if s == 0 and d[s]>=3:
                        ans.append([nums[i],nums[j],s])
                    elif s!=0 and (s==nums[i] or s==nums[j]) and d[s]>=2:
                        ans.append([nums[i],nums[j],s])
                    elif s!=0 and (s!=nums[i] and s!=nums[j]):
                        ans.append([nums[i],nums[j],s])
                j+=1    
        return ans
                    
        