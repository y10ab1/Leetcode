class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            if target <= matrix[i][-1]:
                idx = bisect.bisect_left(matrix[i], target)
                if matrix[i][idx] == target:
                    return True
        return False       