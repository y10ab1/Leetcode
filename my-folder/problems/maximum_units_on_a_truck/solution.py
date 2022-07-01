class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total = 0
        for n, u in boxTypes:
            if truckSize >= n:
                truckSize -= n
                total += u*n
            else:
                total += u*truckSize
                break
        return total