class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = "".join(sorted(str(n))) 
        for p in range(32):
            if target == "".join(sorted(str(2**p))):
                return True

        return False
        