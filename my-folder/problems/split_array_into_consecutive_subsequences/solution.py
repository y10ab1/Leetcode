class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = Counter(nums)
        end = Counter()
        
        for n in nums:
            if left[n] == 0: continue
            left[n] -= 1
            if end[n-1] > 0:
                end[n-1] -= 1
                end[n] += 1
            elif left[n+1] > 0 and left[n+2] > 0:
                left[n+1]-=1
                left[n+2]-=1
                end[n+2]+=1
            else:
                return False
        return True