class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        res = []
        for n in nums:
            if n %2==0:
                evenSum+=n
        
        for v,i in queries:
            toadd = nums[i]+v
            if nums[i]%2==0:
                evenSum-=nums[i]
            if toadd%2==0:
                evenSum+=toadd
            nums[i] = toadd
            res.append(evenSum)
        
        return res