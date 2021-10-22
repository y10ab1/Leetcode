class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def SetA(i,j):
            if matrix[i][0] != 'A':
                for ii in range(len(matrix[0])):
                    if matrix[i][ii] != 0:
                        matrix[i][ii] = 'a'
                if matrix[i][0] != 0:
                    matrix[i][0] = 'A'
            
            if matrix[0][j] != 'B':
                for jj in range(len(matrix)):
                    if matrix[jj][j] != 0:
                        matrix[jj][j] = 'b'
                if matrix[0][j] != 0:
                    matrix[0][j] = 'B'
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    SetA(i,j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'a' or matrix[i][j] == 'A' or matrix[i][j] =='B' or matrix[i][j] =='b':
                    matrix[i][j] = 0
                    
        