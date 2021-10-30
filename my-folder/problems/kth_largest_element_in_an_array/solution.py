class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        '''def it(l, r):
            p = nums[r]
            check = l
            for i in range(l,r):
                if nums[i] < p:
                    nums[i], nums[check] = nums[check], nums[i]
                    check+=1
            nums[check], nums[r] = nums[r], nums[check]
            return check
                    
                
                
        L, R = 0, len(nums)-1
        while True:
            idx = it(L, R)
            if len(nums)-idx < k:
                R, L = idx-1, 0
            elif len(nums)-idx > k:
                L, R = idx+1, len(nums)-1
            else:
                return nums[idx]'''
        nums.sort()
        return nums[len(nums)-k]
        