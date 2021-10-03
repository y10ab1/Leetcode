class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        out = []
        for n in nums1:
            try :
                d[n]+=1
            except:
                d[n]=1
        for n in nums2:
            try:
                if d[n] > 0:
                    out.append(n)
                d[n]-=1
                
            except:
                pass
        return out
                