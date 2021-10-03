class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if len(nums2) == 0:
            return
        
        for i in range(n):
            nums1.insert(0,nums1.pop())
        
        id1 = 0
        id2 = 0
        idx = 0
        
        while idx < m+n:
            if id1<m and id2<n:
                if nums1[id1+n] < nums2[id2]:
                    nums1[idx] = nums1[id1+n]
                    idx+=1
                    id1+=1
                else:
                    nums1[idx] = nums2[id2]
                    idx+=1
                    id2+=1
            elif id2>=n:
                nums1[idx:] = nums1[id1+n:]
                return
            elif id1>=m:
                nums1[idx:] = nums2[id2:]
                return
        
            
            
        
        