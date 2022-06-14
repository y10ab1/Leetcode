class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        acc = defaultdict(int)
        maxvalue = 0
        for i in nums:
            acc[i] += i
            maxvalue = max(maxvalue, i)
        

        keys = sorted(acc.keys())
        
        b2 = 0
        b1 = acc[keys[0]]
        
        for i in range(1, len(keys)):
            cur = keys[i]
            if cur == keys[i-1]+1:
                b2, b1 = b1, max(b1, b2+acc[cur])
            else:
                b2, b1 = b1, b1+acc[cur]
        
        return b1