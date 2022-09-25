class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(list)
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                d[nums[i]*nums[j]].append(set([nums[i],nums[j]]))
        
        for k in d.keys():
            if len(d[k]) > 1:
                for i in range(len(d[k])):
                    for j in range(i+1,len(d[k])):
                        if len(d[k][i] & d[k][j]) == 0:
                            ans+=8
        return ans
