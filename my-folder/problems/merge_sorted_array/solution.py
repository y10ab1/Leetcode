class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if len(nums2) == 0:
            return
        
        for i in range(n):
            nums1.insert(0,nums1.pop())
        
        a, b, c = 0, 0, 0
        
        
        while c < m+n :
            if a<m and b<n:
                if nums1[a+n] < nums2[b]:
                    nums1[c] = nums1[a+n]
                    a+=1
                    c+=1
                else:
                    nums1[c] = nums2[b]
                    b+=1
                    c+=1
            elif a==m and b<n:
                nums1[c] = nums2[b]
                b+=1
                c+=1
            elif a<m and b==n:
                nums1[c] = nums1[a+n]
                a+=1
                c+=1
        
            
            
        
        