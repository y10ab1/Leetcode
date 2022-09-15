class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left[i] -> product of all elements before i'th
        # right[i] -> product of all elements after i'th 
        
        n = len(nums)
        left, right = [1]*n, [1]*n
        
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        
        
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
            
        ans = []
        for i in range(n):
            ans.append(left[i]*right[i])
        
            
        # left [1,1,2,6]
        # right [24,12,4,1]
        return ans
        # time: O(n)
        # space: O(n)