class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        res = 0
        for g,p in sorted(zip(growTime, plantTime)):
            res = max(res,g)+p
        return res