class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        si, sj = 0, len(matrix[0])-1
        while si<len(matrix) and sj>=0:
            if matrix[si][sj] < target:
                si+=1
            elif matrix[si][sj] > target:
                sj-=1
            else:
                return True

        return False