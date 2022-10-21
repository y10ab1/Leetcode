class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        l = deque([])
        s = set()
        for n in nums:
            
            if n in s:
                return True
            l.append(n)
            s.add(n)
            if len(l) > k:
                s.remove(l.popleft())
        return False
            