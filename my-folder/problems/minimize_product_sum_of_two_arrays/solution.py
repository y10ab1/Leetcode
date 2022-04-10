class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        ans = 0
        for i in range(len(nums1)):
            ans += nums1[i] * nums2[len(nums1) - i-1]
        return ans