class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums1)%2==0 and len(nums2)%2==0:
            return 0
        elif len(nums1)%2==1 and len(nums2)%2==0:
            for n in nums2:
                ans^=n
            return ans
        elif len(nums1)%2==0 and len(nums2)%2==1:
            for n in nums1:
                ans^=n
            return ans
        elif len(nums1)%2==1 and len(nums2)%2==1:
            for n in nums2:
                ans^=n
            for n in nums1:
                ans^=n
            return ans