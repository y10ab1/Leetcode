class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        p = [[10001]]
        ans = 1
        for n in nums:
            l, r = 0, ans-1
            while l < r:
                m = (l+r)//2
                if n <= p[m][-1]:
                    r = m
                elif n > p[m][-1]:
                    l = m+1
            if n <= p[l][-1]:
                p[l].append(n)
            elif n > p[l][-1]:
                p.append([n])
                ans+=1
        return ans
            
        