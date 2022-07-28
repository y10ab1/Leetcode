class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for tt in t:
            d[tt] += 1
        for ss in s:
            d[ss] -= 1
        for v in d.values():
            if v != 0:
                return False
        return True