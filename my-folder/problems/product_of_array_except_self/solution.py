class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left[i] -> product of all elements before i'th
        # right[i] -> product of all elements after i'th 
        
        n = len(nums)
        left, right = [1]*n, [1]*n
        
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
            right[n-1-i] = right[n-i] * nums[n-i]
            
        ans = []
        for i in range(n):
            ans.append(left[i]*right[i])
        

        return ans
        # time: O(n)
        # space: O(n)